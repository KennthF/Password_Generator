import random

def number_generate():
    print(random.randrange(0, 9)) 

def symbol_gen():
    """ Symbols is from 33 to 47, 58 to 64 """
    for i in range(33,55):
        if i >= 48:
            i+=10
        print(chr(i))

def letters_gen():
    """ Letters is from 65 to 90 (Big), 61 to 69 then 6A then 6F, 70 to 79, then 7A (small)"""
    pass

#I think its better to make a list instead 

