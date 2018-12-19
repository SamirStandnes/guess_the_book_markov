from time import sleep
from random import randint

def status(user, score):
	return str(user) + "'s score is: " + str(score)	


def game_run(book_input, user, num_runs=0):
	num_runs = num_runs
	solution = str(book_input['title'] + " " + book_input['author'] + " " + book_input['author_initials']).lower()
	option = raw_input('To guess press G, to get a hint press H, to quit press Q: ').upper()
	if option == 'G':
		#print num_runs
		sleep(2)
		guess = raw_input('Guess: ')
		if guess.strip().lower() in solution:
			print 'Correct, the book is ' + book_input['title'] + 'written by ' + book_input['author']
			print status(user, num_runs)
		else:
			print "Wrong..."
			num_runs += 1
			#print num_runs
			game_run(book_input, user, num_runs)		
	elif option == 'H':
		num_runs += 1
		#print num_runs
		print 'Passage: \n' + book_input['passage'] + '\n'
		print 'Initials:' + book_input['author_initials'] + '\n'
		sleep(1)
		guess = raw_input('Guess: ').strip().lower()
		if guess in solution and len(guess) > 1:
			print 'Correct, the book is ' + book_input['title'] + '  written by ' + book_input['author']
			print status(user, num_runs)
			#print num_runs
		else:
			print 'Wrong....'
			num_runs += 1
			game_run(book_input, user, num_runs)			
	elif option == "Q":
		print status(user, num_runs)
		print "Quitting round...."
		sleep(1)
	else:
		print "error...running again"
		game_run(book_input, user, num_runs)
		
		
# test solution by printin solution variable		
