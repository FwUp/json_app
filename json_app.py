import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean {} instead?".format(get_close_matches(w, data.keys())[0])
    else:
        return "The {} is not in library".format(w)

word = input("Enter word: ").lower()

print(translate(word))