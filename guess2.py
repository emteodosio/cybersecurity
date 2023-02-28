#!/usr/bin/python3

import random

 

userguess1 = tuple(input("Enter 1st number: "),"Enter 2nd number: ")

myguess = random.randint(userguess1)

print("Is your number " + int(myguess) + "?")

if(myguess == userguess):

    print("I guessed your number!")

else:

    print("Oh, I guessed incorrectly!")

 