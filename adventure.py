#!/usr/bin/env python
#
# Welcome to the Caverns of Gwimble adventure
# Copyright (C) Robin 'Neoinr' Elden 2012
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
import time
import random
def space(amount): # easter egg :3
        #Prints sp, the number of a's, and ce
        print "%s%s%s" % ('Sp','a'*amount,'ce')
def prompt(): # prompt that's called for input
 try:
	choice = raw_input(">  ") # gets data from player -- NOTE: Change symbol?
	if choice == "exit": # exit clause
		print "Thank you for playing."
		exit()
	elif choice == "help": # No help :P
		print "Help comes to those who find it."
		return choice
	elif choice == "sudo": # Easter eggs for the win
		print "I'm sorry, root access is not available. Cheater."
		return choice
	elif "spa" in choice: # Portal for the win
		print "Greetings."
		print "What is your favourite number?"
		spacestr = raw_input("#  ") # Get the string
		spaceint = int(spacestr) # make the string into an integer
		if spaceint == 42:
			print "You chose the perfect number!" # Hitchhiker's guide to the galaxy
			space(42)
			win("combining the meaning of life, the universe, and everything, with spaaaaace")
		else:
			space(spaceint)
			return choice
	else:
		return choice # Send back the choice
 except (KeyboardInterrupt, EOFError):
	exit("Sorry to see you go :(")
def start(): # start message
	print "Welcome to the Caverns of Gwimble adventure, by Robin Elden"
	time.sleep(0.5)
	print "You wake up, slowly. As your thoughts crystalize, you realise you have no knowledge of who you are, or how you got here. You stand up off the stone floor and look around."
	time.sleep(1)
	print "The room is bare. There is a torch, attached to the wall, giving off a dim light, and 3 doors, ahead, to the right, left, and forward."
	bare_room() # To the first room
def bare_room(): #first room
	go = prompt() # gets the choice 
	if go.upper() == 'LEFT':
		print "As you go through the door, it slams behind you. You turn to look, but see only a blank section of wall behind you."
		print "This room is an immense treasure room. Piles of gold and gems tower throughout. There is a sleeping dragon lying in the centre of the room. There is a small stick, and a heavy rock, resting by your feet. You consider throwing something at the dragon."
		dragon_room() # puts the description beforehand so it's not repeated if invalid input
	elif go.upper() == 'RIGHT': 
		other_room() # not actually a room
	elif go.upper() == 'FORWARD': 
		forward_room()
	elif go.upper() == 'LOOK':
		print "I've already told you what you see."
		bare_room()
	elif go.upper() == 'LOOK CAREFULLY':
		print 'You see a small stone button on one of the walls. The button says "Do not press me".'
		bare_room()
	elif go.upper() == 'PRESS BUTTON':
		print "You suddenly realise why you shouldn't have pressed the button, as the whole universe fad-"
		time.sleep(5)
		alternate()
	else:
		print "You are still here."
		bare_room()
def alternate(): # Alternate reality
	print "\fWelcome to the Gardens of Froob"
	print "You spring out of bed, eyes alert and eager for the world beyond"
	print "The room is colorful, full of paint and decorations" 
	prompt()
	print "Before you can do anything, you realise that something is wrong."
	print "You should not be here, it feels alien to you."
	die("existential crisis, consequences of meddling with the space-time continuum")
def dragon_room(): # NOTE: I should add more options
	do = prompt()
	if "stick" in do:
		print "The stick vanished before you were able to do anything."
		dragon_room()
	elif "rock" in do:
		print "You pick up the rock. The dragon, hearing the noise, activates mind control"
		free_your_mind() # and the rest will follow
	elif "eat" in do:
		print "Eat what? The dragon looks a bit stringy."
		dragon_room()
	elif "take gold" in do:
		print "You attempt to take some of the gold. The dragon stirs, instantly alert."
		print "The last thing you feel is a blinding heat as you are incinerated."
		die("being incinerated by dragonfire")
	else:
		print "I don't know what you mean"
		dragon_room()
		
def free_your_mind():
	print "To free your mind, you must think of a number between 1 and 10. If you guess right, you live."
	tehnum = str(random.randint(1, 10))
	print tehnum
	num = int(prompt())
	print num
	if num == tehnum:
		print "You overcome the mind control and use your superior intellect to beat the dragon into submission. The dragon falls over, dead."
		win("triumph over an evil dragon")
	elif 1 >= num <= 10:
		print "You guess wrong. The dragon overcomes your mind."
		die("having your mind crushed by a dragon")
	else:
		print "I said between 1 and 10, moron"
		die("being a moron")
def win(arg1):
        print "."
        time.sleep(0.3)
        print "."
        time.sleep(0.3)
        print "."
        time.sleep(0.3)
	print "Congratulations. Your achievement, %s, has won you the game!" % arg1
	print "What is your name?"
	name = raw_input(">  ")
	score = "Winner: " + name + "(won by " + arg1 + ")\n"
	file=open("scores.txt", "a")
	file.write(score)
	print "Thanks for completing Caverns of Gwimble"
	exit()
def die(arg2):
	print "."
	time.sleep(0.3)
        print "."
        time.sleep(0.3)
        print "."
        time.sleep(0.3)
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
	print "The Door Network apologises for any inconvience, but this door is temporarily phased out of existence."
	print "If you have a manual override code, please enter it now:"
	code = prompt()
	print code
	if code == "1337":
		print "Code accepted."
		print "Please select destination:"
		print "1. Starting room"
		print "2. Dragon room"
		print "3. Deity room"
		print "4. Alternate reality"
		print "5. Space"
		des = prompt()
		if des == "1":
			bare_room()
		elif des == "2":
			dragon_room()
		elif des == "3":
			forward_room()
		elif des == "4":
			alternate()
		elif des == "5":
			inspace()
		else:
			print "Invalid destination"
			other_room()
	else:
		print "I'm sorry, that code is incorrect."
		print "You are teleported back to the starting room" 
		bare_room()
def forward_room():
	print "You step forward, into a room of pure white light. You hear a booming voice."
	print "VOICE: Congratulations, young adventurer."
	print "VOICE: I will grant you immortality, if you can correctly answer this question."
	print "VOICE: Complete the sentence: The ____ is a lie"
	cake = prompt()
	if cake == "cake":
		print "VOICE: That is correct."
		win("becoming immortal") # WIN!
	else:
		print "VOICE: That is not correct." # NOTE: Not sure about the VOICE
		print "You feel your organs liquify, and lose consciousness"
		die("being liquified") # NOTE: Would a deity liquify someone?
def inspace():
	print "\f" #Clear the screen to indicate change of location
	print "You are in space"
	time.sleep(1)
	print "You are suffocating..."
	time.sleep(1)
	die("lack of oxygen")
print "\f" # Clear the screen
start()
