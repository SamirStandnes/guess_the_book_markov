from time import sleep

def intro():
	user = raw_input("Hi and welcome....please enter your name: " ).capitalize()
	rules = 'You start off with 0 points. The goal of the game is to guess the correct book and/or author. For each guess that is incorrect, your score will be increased by one point. You will also add points everytime you request a hint. Good luck ' + user + "!\n"
	sleep(1)
	print "The rules are as follows: \n" + rules
	sleep(1)
	print "Let's go " + user + "! \n"
	sleep(1)
	print "First genereated text, try to guess the author and/or the book: \n"
	sleep(1)
	return user