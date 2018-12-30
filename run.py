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

books_list = ['http://www.gutenberg.org/files/11/11-h/11-h.htm', 'http://www.gutenberg.org/files/2701/2701-h/2701-h.htm', 'http://www.gutenberg.org/files/1342/1342-h/1342-h.htm', 'http://www.gutenberg.org/files/76/76-h/76-h.htm', 'http://www.gutenberg.org/files/1080/1080-h/1080-h.htm', 'http://www.gutenberg.org/files/1497/1497-h/1497-h.htm', 'http://www.gutenberg.org/files/1322/1322-h/1322-h.htm', 'http://www.gutenberg.org/files/1184/1184-h/1184-h.htm', 'http://www.gutenberg.org/files/16/16-h/16-h.htm', 'http://www.gutenberg.org/files/3207/3207-h/3207-h.htm','http://www.gutenberg.org/files/2814/2814-h/2814-h.htm','http://www.gutenberg.org/files/236/236-h/236-h.htm', 'http://www.gutenberg.org/files/4363/4363-h/4363-h.htm']

#fetching_data test
def data_fetch_test():
	for i in range(len(books_list)):
		data = get_book_data(books_list[i])
		print data['passage'], data['author'], data['author_initials'], books_list[i], 'index_booklist: ' + str(i)
		# optional textify_markov test
		"""
		book = get_book_data(books_list[i])
		mc = MarkovChain()
		mc.add_string(book['text'])
		print textify_markov(mc.generate_text(10))
		"""
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
			game_run(book,user)
			option = raw_input('Want to run another round with different books? Enter Y/N: \n').upper()
		else:
			run = False
		print "Number of books left: " + str(len(books_list))
	else:
		print "Ending game..."
		sys.exit()

program()
