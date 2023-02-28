#!/usr/bin/python3

# The following line creates an empty variable
number=""
# basenum=""

while(not(number.isnumeric())):
    number = input("What is the decimal to convert? ")
#   basenum = input("Which basenum? (hex, Octal, )")

# Conversion table of remainders to
# hexadecimal equivalent
# basenum = datatype()

tempnumb = int(number)
bin_output = ""

while(tempnumb > 0):
    bin_output = str(tempnumb % 2) + bin_output
    tempnumb = int(tempnumb / 2)

# if basenum="hex"
# hex_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',5: '5', 6: '6', 7: '7',8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',13: 'D', 14: 'E', 15: 'F'}

print (bin_output)