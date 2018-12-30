from bs4 import BeautifulSoup
from random import randint
import urllib2
import re

def get_book_data(book_url):
	response = urllib2.urlopen(book_url)
	soup = BeautifulSoup(response, 'html.parser')
	html_as_string = ''
	paragraphs = soup.find_all('p')
	for par in paragraphs:
		html_as_string += par.get_text().encode('utf-8')
	soup_title = soup.title.get_text().split(',')
	title = soup_title[0].strip().encode('utf-8')
	author = soup_title[1].replace("By", "").replace("by", "").strip().encode('utf-8') if soup_title[1].strip().lower().startswith("by") else "Error author name"
	author = ' '.join(filter(lambda x: re.match("(^\w)", x), author.split()))
	author_initials =  '.'.join([x[0] for x in author.split(" ")]).encode('utf-8') if author.startswith("Error") == False else "Error author name"
	passage = paragraphs[randint(0, len(paragraphs)-1)].get_text()

	return { 'text': html_as_string,
			 'title': title,
			 'author': author,
			 'author_initials': author_initials,
			 'passage': passage	 }



#data_fetch_test ref. run file comment to book_list variable
