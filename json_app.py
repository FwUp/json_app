import json

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        return "The {} is not in library".format(w)

word = input("Enter word: ")

print(translate(word))