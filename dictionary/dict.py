####################################################################################################
#
# Basic Dictionary app from command line.
# Enter your word and get the information.
#
# get_close_matches: difflib.get_close_matches(word,possibilities,n,cutoff)
#     Return a list of the best “good enough” matches.
#        word is a sequence for which close matches are desired (typically a string), 
#        possibilities is a list of sequences against which to match word (usually a list of strings).
#        [Optional] n (default 3) is the maximum number of close matches to return; n > 0
#        [Optional] cutoff (default 0.6) is a float in the range [0, 1]. 
#            difflib.SequenceMatcher.ratio() gives a similarity ratio
#            Possibilities that don’t score at least that similar to word are ignored. 
#
####################################################################################################

import json
from difflib import get_close_matches


data = json.load(open("dict.json"))


def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	elif len(get_close_matches(w, data.keys())) > 0:
		best_choice = get_close_matches(w, data.keys())[0]
		yesno = input("Did you mean %s instead? Enter Y if yes , or N if no:" % best_choice).lower()
		if yesno == 'y':
			return data[best_choice]
		elif yesno == 'n':
			return "The word doesn't exist. PLease check!."
		else:
			return "We didn't understand your entry"
	else:
		return "The word doesn't exist. Please check!."



word = input("Enter your word: ")

print(translate(word))
