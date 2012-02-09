def prompt():
	choice = raw_input(">  ")

	if choice == "exit":
		print "Thank you for playing."
		exit()
	elif choice == "help":
		print "Help comes to those who find it."
		return "null"
	else:
		return choice
def start():
	print "Welcome to the Caverns of Gwimble adventure, by Robin Elden"
	print "You wake up, slowly. As your thoughts crystalize, you realise you have no knowledge of who you are, or how you got here. You stand up off the stone floor and look around."
	print "The room is bare. There is a torch, attached to the wall, giving off a dim light, and 3 doors, ahead, to the right, and left."
	bare_room()
def bare_room():
	go = prompt()
	if go == "Left" or go == "left":
		print "As you go through the door, it slams behind you. You turn to look, but see only a blank section of wall behind you."
		print "This room is an immense treasure room. Piles of gold and gems tower throughout. There is a sleeping dragon lying in the centre of the room. There is a small stick, and a heavy rock, resting by your feet. You consider throwing something at the dragon."
		dragon_room()
	elif go == "Right" or go == "right":
		other_room()
	elif go == "Forward" or go == "forward":
		forward_room()
	elif go == "null":
		bare_room()
	else:
		print "I do not understand your choice."
		bare_room()

def dragon_room():
	do = prompt()
	if "stick" in do:
		print "The stick vanishes before you able to do anything."
	if "rock" in do:
		print "You pick up the rock. The dragon, hearing the noise, activates mind control"
		free_your_mind()
	if "eat" in do:
		print "Eat what? The dragon looks a bit stringy."
		dragon_room()
	else:
		print "I don't know what you mean"
		dragon_room()
		
def free_your_mind():
	print "To free your mind, you must think of a number between 1 and 10. If you guess right, you live."
	num = prompt()
	if num == "7":
		print "You overcome the mind control and use your superior intellect to beat the dragon into submission. The dragon falls over, dead."
		win("triumph over an evil dragon")
	if num == "1" or num == "2" or num == "3" or num == "4" or num == "5" or num == "6" or num == "8" or num =="9" or num == "10":
		print "You guess wrong. The dragon overcomes your mind."
		die("having your mind crushed by a dragon")
	else:
		print "I said between 1 and 10, moron"
		die("being a moron")
def win(arg1):
	print "Congratulations. Your achievement, %s, has won you the game!" % arg1
	print "What is your name?"
	name = raw_input(">  ")
	score = "Winner: " + name + "(won by " + arg1 + ")\n"
	file=open("scores.txt", "a")
	file.write(score)
	print "Thanks for completing Caverns of Gwimble"
	exit()
def die(arg2):
	print "You have died from: %s" % arg2
        print "What is your name?"
        name = raw_input(">  ")
        score = "Loser: " + name + "(died by " + arg2 + ")\n"
        file=open("scores.txt", "a")
        file.write(score)
	print "Thanks for completing Caverns of Gwimble"
	exit()
def other_room():
	print "There is no door, only Zuul"
	bare_room()
def forward_room():
	print "You step forward, into a room of pure white light. You hear a booming voice."
	print "VOICE: Congratulations, young adventurer."
	print "VOICE: I will grant you immortality, if you can correctly answer this question."
	print "VOICE: Complete the sentence: The ____ is a lie"
	cake = prompt()
	if cake == "cake":
		print "VOICE: That is correct."
		win("becoming immortal")
	else:
		print "VOICE: That is not correct."
		print "You feel your organs liquify, and lose consciousness"
		die("being liquified")
start()
