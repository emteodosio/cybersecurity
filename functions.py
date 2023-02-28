'''
#Code 1
#!/usr/bin/python3
import math

def area_of_circle(rad):
    return round(math.pi * rad**2,2)

def circumference_of_circle(rad):
    return round(math.pi * 2 * rad,2)

if __name__ == '__main__':
    radius = int(input("What is the radius? ")) 
    print("The area is", area_of_circle(radius))
    print("The circumference is", circumference_of_circle(radius))
'''

'''
#Code 2
#!/usr/bin/python3
import random

noun=("car","bus","ball","plane","cup")
verb=("jump","sit","run","think","smile")
superhero=("Superman","Wonder Woman","Batgirl","Batman")
animal=("dog","cat","octopus","wolverine","snail","monkey")
people=("Abe","Jim","Gary","Michelle","Kimberly","Megan","Omar")
places=("the Citadel Mall","Denver","North Pole","downtown")
season=("spring","winter","fall","summer")

def elem(tuple):
    value = random.randint(0,len(tuple)-1)
    return tuple[value]

if __name__ == '__main__':
    print("Every " + elem(season) + ", " + elem(superhero) + \
    " is joined by The " + elem(animal) + \
    ", who's secret identity is " + elem(people) + \
    ". They attempt to " + elem(verb) +\
    ", which rarely succeeds.  So instead they chase down a " + \
    "villain in " + elem(places) + " who was trying to steal a " + \
    elem(noun) + ".")
'''

'''
#Code 3
#!/usr/bin/python3

def bool (a,b):
    return (a == b)

if __name__ == '__main__':
    val_a = input("What is the first value? ")
    val_b = input("What is the second value? ")

    print(bool(val_a,val_b))
'''

#Code-Lab
#!/usr/bin/python3
import random

noun=("car","bus","ball","plane","cup")
verb=("jump","sit","run","think","smile")
superhero=("Superman","Wonder Woman","Batgirl","Batman")
animal=("dog","cat","octopus","wolverine","snail","monkey")
people=("Abe","Jim","Gary","Michelle","Kimberly","Megan","Omar")
places=("the Citadel Mall","Denver","North Pole","downtown")
season=("spring","winter","fall","summer")

def elem(tuple):
    value = random.randint(0,len(tuple)-1)
    return tuple[value]

if __name__ == '__main__':
    print("Every " + elem(season) + ", " + elem(superhero) + \
    " is joined by The " + elem(animal) + \
    ", who's secret identity is " + elem(people) + \
    ". They attempt to " + elem(verb) +\
    ", which rarely succeeds.  So instead they chase down a " + \
    "villain in " + elem(places) + " who was trying to steal a " + \
    elem(noun) + ".")