import random
import string

alpha, symbols, num = string.ascii_letters, string.punctuation, string.digits

def get_len(item):
    """ Get the length of the list """
    return len(item) - 1

def pass_form(length):
    password = ""
    print(length)

def main():
    user = ""
    while user == "":
        print("\nWelcome to Random Password Generator\n")
        user = input("  ~~ Include Digit (y or n): ")
        user += input("  ~~ Include Symbols (y or n): ")
        user += input("  ~~ Password's Length: ")
        user = user.lower().strip()
        user_len = get_len(user) + 1

        if not user[0] == "y" and not user[0] == "n":
            print("\n ~~ Invalid Input for Digit ~~ \n".upper())

        elif not user[1] == "y" and not user[1] == "n":
            print("\n ~~ Invalid Input for Symbol ~~ \n".upper())
        
        elif user_len > 4 and not user[3].isdigit():
            print("\n ~~ Password's Length is not a valid input ~~ \n".upper())
            print(user)

        elif not user[3:user_len].isdigit:
            print("\n ~~ Password's Length is not a valid input ~~ \n".upper())
            print(user)

        else:
            pass_form(user)
        
        user = ""



main()



