from os import *
def clearTerminal():
    system("clear")
def printDice(number):
    if number <= 6:
        if number == 1:
            print("ooooooooooo")
            print("o         o")
            print("o    X    o")
            print("o         o")
            print("ooooooooooo")
        if number == 2:
            print("ooooooooooo")
            print("o  X      o")
            print("o         o")
            print("o      X  o")
            print("ooooooooooo")
        if number == 3:
            print("ooooooooooo")
            print("o  X   X  o")
            print("o         o")
            print("o    X    o")
            print("ooooooooooo")
        if number == 4:
            print("ooooooooooo")
            print("o  X   X  o")
            print("o         o")
            print("o  X   X  o")
            print("ooooooooooo")
        if number == 5:
            print("ooooooooooo")
            print("o  X   X  o")
            print("o    X    o")
            print("o  X   X  o")
            print("ooooooooooo")
        if number == 6:
            print("ooooooooooo")
            print("o  X X X  o")
            print("o         o")
            print("o  X X X  o")
            print("ooooooooooo")
    else:
        print("ooooooooooo")
        print("o         o")
        print("o    ?    o")
        print("o         o")
        print("ooooooooooo")
def sum(a, b):
    return a + b
def difference(a, b):
    return a - b
def product(a, b):
    return a * b
def quotient(a, b):
    return a / b
def Celcius(t):
    return (t - 32) * (5/9)
def Fahrenheit(t):
    return ((9/5)(t) + 32)
def ask(question):
    return(input(str(question) + ": "))
