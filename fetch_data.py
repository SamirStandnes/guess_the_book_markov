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

		


#
#from cc_markov import MarkovChain
#print html.get_text()
#print author
#print author
#print author_initials
#mc = MarkovChain()
#mc.add
#print author_initials
#print books
#print get_book_data()
# 'http://www.gutenberg.org/files/11/11-h/11-h.htm', 'http://www.gutenberg.org/files/2701/2701-h/2701-h.htm', 'http://www.gutenberg.org/files/74/74-h/74-h.htm', http://www.gutenberg.org/files/76/76-h/76-h.htm'
#print get_book_data('http://www.gutenberg.org/files/158/158-h/158-h.htm')
#http://www.gutenberg.org/files/1184/1184-h/1184-h.htm
"""

#from io import BytesIO
#from gtts import gTTS
#import facebook
#import requests
#import ssl 
token = 'EAADzT03XrgYBACW4m3hvqIlRGecMr0YunnNoTPZBap57IfoGf3JBIZB6BkZCe7Yr50YZBYkomTZCrRcg6mUQPpZAsUE2fWVOUCV0YtvAHdV0V0dMKy5M5xwxlcsk3aFAb0t9pDvfFPK0x8xFJc3DQ2QUgu00XV6vTtHG5GphlHMkpepYF9q7teJRfvo3BOjhOtLmkqZAWq881lq5pMpOQJEARF8AIU6jmWKknBQuiPpzwZDZD'

graph = facebook.GraphAPI(access_token=token, version = 3.1)

user = graph.request('/me?fields=id,name,first_name, last_name, picture')

print user
#print mc.generate_text(10)

# testing change + Testing chaning in push directory
mp3_fp = BytesIO()
tts = gTTS('Hello', 'en')
tts.write_to_fp(mp3_fp)

"""