import json
import os
import sys
import time
from subprocess import call
from difflib import get_close_matches

# load json data
data = json.load(open("data.json"))

# clear screen function
def clear_screen():
    i = call('clear' if os.name == 'posix' else 'cls')

# main function
def translate(w):
    clear_screen()
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
            clear_screen()
            return data[get_close_matches(w, data.keys())[0]]
        elif answer == "N" or answer == "n":
            clear_screen()
            return "The \"{}\" doesn't exist in dictionary.Please double check it.".format(word)
        elif answer.isdigit():
            clear_screen()
            return "That's a number fool,only words are allowed"
        else:
            return "We didn't understand your entry."
    elif  w.isdigit(): # check numbers
        return "That's a number fool,only words are allowed"
    else:
        return "The \"{}\" is not in dictionary".format(w)

def menu():
    print("Main Menu")
    choice = input("""
            Q:quit program
            S:start dictionary
            M:main menu
Please enter your choice: """).lower()
    if choice == 'q':
        clear_screen()
        time.sleep(3)
        print("Good Bye\nExiting...")
        sys.exit
    elif choice == 's':
        word = input("Enter word: ")
        output = translate(word)

        if type(output) == list: # check if output is list data type
            for i in output:
                print(i)
        else:
            print(output)
    elif choice == 'm':
        clear_screen()
        menu()
    else:
        print("Wrong choice")
        menu()
        
menu()