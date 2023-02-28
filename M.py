#!/usr/bin/python3


#M = 0
#L = [3,16,2,93,-5,0,17]
#for num in L:
#    if num > M:
#        M = num
#print(M)
#

myval = ""
while (myval.isdigit() == False):
    myval = input("Number?")
    
if (int(myval) in range(0,10)):
    print(myval,"is between 0 and 10")
else:
    print(myval,"is less than 0 or greater than 10")