from fetch_data import get_book_data
from cc_markov import MarkovChain
from textify import textify_markov
from time import sleep
from random import randint
from round import game_run, status
from intro import intro
import sys

"""

Adding books from gutenberg.org -- ones that fit the format. Correct format is usually ones from the popular list. 
Format compatibility can easily be "tested" with the fetch_data function, by printing the return object or
by running the data fetch test below

"""

books_list = ['http://www.gutenberg.org/files/11/11-h/11-h.htm', 'http://www.gutenberg.org/files/2701/2701-h/2701-h.htm', 'http://www.gutenberg.org/files/1342/1342-h/1342-h.htm', 'http://www.gutenberg.org/files/76/76-h/76-h.htm', 'http://www.gutenberg.org/files/1080/1080-h/1080-h.htm', 'http://www.gutenberg.org/files/1497/1497-h/1497-h.htm', 'http://www.gutenberg.org/files/1322/1322-h/1322-h.htm', 'http://www.gutenberg.org/files/1184/1184-h/1184-h.htm']

#fetching_data test
def data_fetch_test():
	for i in range(len(books_list)):
		print get_book_data(books_list[i])
		# optional textify_markov test
		book = get_book_data(books_list[i])
		mc = MarkovChain()
		mc.add_string(book['text'])
		print textify_markov(mc.generate_text(10))
	
#data_fetch_test()

def program():
	run = True	
	while run:
		book_url = books_list[randint(0, len(books_list)-1)]
		print "Number of books left: " + str(len(books_list))
		book = get_book_data(book_url)
		user = intro()
		mc = MarkovChain()
		mc.add_string(book['text'])
		print '"' + textify_markov(mc.generate_text(15)) + '" \n'
		#result = game_run(book, 0) 
		game_run(book, user)
		sleep(1)
		option = raw_input('Want to run another round with a different book? Enter Y/N: \n').upper()
		while option == 'Y':
			books_list.remove(book_url)
			book_url = books_list[randint(0, len(books_list)-1)]
			book = get_book_data(book_url)
			mc = MarkovChain()				
			mc.add_string(book['text'])
			print '"' + textify_markov(mc.generate_text(15)) + '"'
			#result = game_run(book)
			game_run(book,user)
			option = raw_input('Want to run another round with different books? Enter Y/N: \n').upper()
		else:
			run = False			
		print "Number of books left: " + str(len(books_list))
	else:
		print "Ending game..."
		sys.exit()
			
program()




"""
# Testing my textify method here
def textify_test():
	print textify_markov(['i'])
	
textify_test()
"""



"""
book_url = books_list[0]
book = get_book_data(book_url)
mc = MarkovChain()				
mc.add_string(book['text'])

markov_text = c.generate_text(15)
print '"' + textify_markov(markov_text) + '"'
print '"' + textify_markov(mc.generate_text(15)) + '"'
"""


"""
mc = MarkovChain()
mc.add_string(book['text'])

print textify_markov(mc.generate_text(15))
"""

#print textify_markov_text(mc.generate_text(10))
#print book['title'], book['passage']

"""
print 'If you can guess the title of this book, I must admit you are good.'

sleep(1)

print "you will be given a generated text, based on the style of an author in a particular book. Guess the right book or author and you win"
user 
"""

"""
mc = MarkovChain()

mc.add_string(book.text)

mc.generate_text(10)
"""
"""
print "If you can guess the title of this book, I must admit you are good. \n I will give you the change to talk to the man himself, and maybe you will find yourself....."



print h
guess = raw_input(
print mc.generate_text(10)
"""

"""
	for i in range(len(generated_text):
		if generated_text[i] in exclude_word:
			generated_text[i].pop()
		elif word == 'i' and len(word) < 2:
			string += word.upper() + ' '
		else:
			string += word + ' '
		print string
	
	re.sub(u"(\u2018|\u2019)", "'", string)
	return string.capitalize()
	"""