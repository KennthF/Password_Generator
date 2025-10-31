import random
import string

alpha, symbols, num = string.ascii_letters, string.punctuation, string.digits

def get_len(item):
    """ Get the length of the list """
    return len(item) - 1

def pass_form(input,len):
    """ Generates a Random Password"""
    count, al_range, password = 0, "", ""

    while count != len:
        #Get which is allowed by the user
        if input[0] == 'y' and input[1] == 'y': #Digit & Symbol
            al_range = random.randrange(0,3)

        elif input[0] == 'y': #Digit
            al_range = random.randrange(0,3,2)
        
        elif input[1] == 'y': #Symbol
            al_range = random.randrange(1,3)

        else:
            al_range = 2
        
        #Creates the password
        match al_range:
            case 0:
                size = get_len(num)
                password += num[random.randrange(0,size)]

            case 1:
                size = get_len(symbols)
                password += symbols[random.randrange(0,size)]

            case 2:
                size = get_len(alpha)
                password += alpha[random.randrange(0,size)]
        
        count += 1
    
    return password
            

    
    

def main():
    user, password = "", ""
    
    while user != "end":
        print("\nWelcome to Random Password Generator\n")
        user = input("  ~~ Include Digit (y or n): ")
        user += input("  ~~ Include Symbols (y or n): ")
        user += input("  ~~ Password's Length: ")
        user = user.lower().strip()
        user_len = get_len(user) + 1

        if user[0] != "y" and user[0] != "n":
            print("\n ~~ Invalid Input for Digit ~~ \n".upper())

        elif user[1] != "y" and user[1] != "n":
            print("\n ~~ Invalid Input for Symbol ~~ \n".upper())
        
        elif user_len > 4 or not user[2].isdigit():
            print("\n ~~ Password's Length is not a valid ~~ \n".upper())

        elif not user[2:user_len].isdigit():
            print("\n ~~ Password's Length is not a valid input ~~ \n".upper())

        else:
            len = int(user[2:user_len])
            password = pass_form(user,len)
        
        print(f"Generates: {password}")

        user = input("\n~~~Type 'End' to end:")

        
main()



