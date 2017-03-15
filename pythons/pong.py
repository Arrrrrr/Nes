from Tkinter import *
import random
import time

# setting up the game board
tk = Tk()
tk.title("do NOT drop the zombie head")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0, bg="grey")
canvas.pack()
tk.update()

# setting up variables that will feed into text for scoring and announcing game over
head_hits = 0
loser = False

# sets up the head gamepiece
class Head:
    def __init__(self, canvas, bat, color):
        self.canvas = canvas
        self.bat = bat
        self.id = canvas.create_oval(0, 0, 30, 30, fill=color)
        # initial motion, randomized
        self.canvas.move(self.id, 245, 200)
        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)
        self.x = starts_x[0]
        self.y = -3
        # sets the playable area
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
	
	# i do not know all the coordinate stuff, but this makes it continue to move
	# it analyzes the current position of self.id and makes a decision on how to change x and y values
	# x makes it move left (-3) and right (3)
	# y makes it move up (3) and down (-3)
    def make_drawing(self):
        self.canvas.move(self.id, self.x, self.y)
        positional = self.canvas.coords(self.id)
        if positional[1] <= 0:
            self.y = 3
        if positional[3] >= self.canvas_height:
            self.y = -3
        if positional[0] <= 0:
            self.x = 3
        if positional[2] >= self.canvas_width:
            self.x = -3
        
        self.bat_positional = self.canvas.coords(self.bat.id)

        # analyzing the position of the head based in relation to the bat
        # and decides based on relationship if you get points / keep playing or if you lose
        if positional[2] >= self.bat_positional[0] and positional[0] <= self.bat_positional[2]:
            if positional[3] >= self.bat_positional[1] and positional[3] <= self.bat_positional[3]:
                self.y = -3
                global head_hits
                head_hits +=1
                score()
        
        if positional[3] <= self.canvas_height:
            self.canvas.after(10, self.make_drawing)
        else:
            game_over()
            global loser
            loser = True

# set up the Bat game piece. "Arl!!!"
class Bat:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 15, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
		# functions move_left and move_right bound to keyboard buttons
		# those two functions will only run when activated by the buttons
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)
	
	# only moves left and right so only has x values
    def make_drawing(self):
        self.canvas.move(self.id, self.x, 0)
        self.positional = self.canvas.coords(self.id)
        if self.positional[0] <= 0:
            self.x = 0
        if self.positional[2] >= self.canvas_width:
            self.x = 0
        global loser
        # re run then function to move the bat if the game is still active
        if loser == False:
            self.canvas.after(10, self.make_drawing)

    def move_left(self, event):
        if self.positional[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.positional[2] <= self.canvas_width:
            self.x = 3

# start the game
def start_game(event):
    global loser, head_hits
    loser = False
    head_hits = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(0.1)
    bat.make_drawing()
    head.make_drawing()
   
# score the game
def score():
    canvas.itemconfig(score_now, text="HEAD HITS: " + str(head_hits))

# end the game
def game_over():
    canvas.itemconfig(game, text="AH!!! YOU DROPPED IT!!!")
    
# now we make actual versions of our game pieces
bat = Bat(canvas, "brown")
head = Head(canvas, bat, "green")

# start scoring
score_now = canvas.create_text(250, 20, text="HEAD HITS: " + str(head_hits), fill = "black", font=("Consolas", 20))

# set up the actual game board
game = canvas.create_text(250, 150, text=" ", fill="black", font=("Helvetia", 40))

# and now we start playing :)
# button 1 means you click your mouse to start playing
canvas.bind_all("<Button-1>", start_game)
tk.mainloop()
