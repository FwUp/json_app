import json
from difflib import get_close_matches

# load json data
data = json.load(open("data.json"))

# main function
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: # check acronyms
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0: # check close matches
        answer = input("Did you mean {} instead?\nEnter Y if yes and N if no: ".format(get_close_matches(w, data.keys())[0]))
        if answer == "Y" or answer == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif answer == "N" or answer == "n":
            return "The \"{}\" doesn't exist in dictionary.Please double check it.".format(word)
        else:
            return "We didn't understand your entry."
    elif  w.isdigit(): # check numbers
        return "That's a number fool,only words are allowed"
    else:
        return "The \"{}\" is not in dictionary".format(w)

word = input("Enter word: ")

output = translate(word)

if type(output) == list: # check if output is list data type
    for i in output:
        print(i)
else:
    print(output)