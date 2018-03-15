```
Basic Dictionary app from command line.
Enter your word and get the information.
```

import json

data = json.load(open(dict.json))


def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	else:
		return "The word doesn't exist. PLease check!."



word = input("Enter your word: ")

print(translate(word))
