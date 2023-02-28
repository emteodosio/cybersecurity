#!/usr/bin/python3

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

word = input("What is the word to encrypt? ").upper()

newletter = ""
newword = ""

for letter in word:
    newletter = alphabet[(alphabet.find(letter) + 3) % 26]
    newword += newletter   

print (word,newword)