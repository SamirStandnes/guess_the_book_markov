list_exclude_sign = ['"', "'", '""', ')', '(', ' " "', '-', '-" "', ' " ',' "', '" ', ' " "']

def change_i(x):
	if x == 'i':
		return 'I'
	else:
		return x
	
def textify_markov(generated_text):
	generated_text = [x for x in generated_text if x not in list_exclude_sign]
	generated_text.append('...')
	generated_text = [change_i(x) for x in generated_text]
	string = ' '.join(generated_text)
	return string.capitalize()
	
	

	