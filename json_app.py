import json, os, sys, time
from subprocess import call
from difflib import get_close_matches

# load json data
data = json.load(open("data.json"))

# menu function
def menu():
    clear_screen()
    print("Main Menu")
    choice = input("""
            Q:quit program
            S:start dictionary
            M:main menu
            L:list all entries that start with choosen letter or letters
Please enter your choice: """).lower()
    if choice == 'q':
        clear_screen()
        print("Good Bye\nExiting...")
        time.sleep(2)
        sys.exit
    elif choice == 's':
        word = input("Enter word: ")
        output = translate(word)

        if type(output) == list: # check if output is list data type
            for i in output:
                print(i)
            q = input("Press m to go to main menu,or q to quit: ").lower()
            if q == 'm':
                clear_screen()
                menu()
            elif q == 'q':
                clear_screen()
                print("Good Bye!")
                time.sleep(1)
                sys.exit
            else:
                print("Wrong choice!!!Exiting...")
                sys.exit
        else:
            print(output)
            main_menu_function()
        
    elif choice == 'm':
        clear_screen()
        menu()
    elif choice == 'l':
        clear_screen()  
        dict(data)     
    else:
        print("Wrong choice!!!")
        time.sleep(3)
        clear_screen()
        menu()
        
# clear screen function
def clear_screen():
    i = call('clear' if os.name == 'posix' else 'cls')

# sort function
def dict(data):
    a = input("Choose a letter: ")
    list = []
    list2 = []
#    clear_screen()
    
    for i in data.keys():
        list.append(i)
        
    for i in list:
        if i.startswith(a):
            list2.append(i)
    
    for i in list2:
        print(i) # print(*list2, sep=",") display items separated by comma
        time.sleep(0.3)
    
    print('\n')
    main_menu_function()

# translate function
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
            return "The \"{}\" doesn't exist in dictionary.Please double check it.".format(w)
        elif answer.isdigit():
            clear_screen()
            return "That's a number fool,only words are allowed"
        else:
            return "We didn't understand your entry."
    elif  w.isdigit(): # check numbers
        return "That's a number fool,only words are allowed"
    else:
        return "The \"{}\" is not in dictionary".format(w)

def main_menu_function():
    q = input("Press m to go to main menu,or q to quit: ").lower()
    if q == 'm':
        clear_screen()
        menu()
    elif q == 'q':
        clear_screen()
        print("Good Bye!")
        time.sleep(1)
        sys.exit
    else:
        print("Wrong choice!!!Exiting")
        sys.exit

menu()