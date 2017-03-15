def clinic():
    print "Where you want me to kick you??? In the balls or in the face??!"
    answer = raw_input("Type balls or face and hit 'Enter'.").lower()
    if answer == "balls" or answer == "b":
        print "Ha! I kicked you in the balls and now you are in lots of pain. Unless you are a girl. Then I kicked you in the face anyway."
    elif answer == "face" or answer == "f":
        print "Your nose is bleeding now!"
    else:
        print "That is not an answer, skaliwag! Try again."
        clinic()

clinic()