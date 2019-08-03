import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        answer = input("Did you mean {} instead?\nEnter Y if yes and N if no: ".format(get_close_matches(w, data.keys())[0]))
        if answer == "Y" or answer == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif answer == "N" or answer == "n":
            return "The \"{}\" doesn't exist in dictionary.Please double check it.".format(word)
        else:
            return "We didn't understand your entry."
    else:
        return "The \"{}\" is not in dictionary".format(w)

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)