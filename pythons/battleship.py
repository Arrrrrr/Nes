# import python library
from random import randint

# set up board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

# start the game
print "Let's play Battleship!"
print_board(board)

# place a battle ship someplace on the board
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# uncomment for cheating
# print ship_row
# print ship_col

# you get 3 turns (0, 1, 2)
for turn in range(3):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    # responses based on your guess
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        print "Turn", turn + 1
        # Game ends if you complete your 3 turns (0, 1, 2)
        if turn == 2:
            print "Game Over"
        print_board(board)