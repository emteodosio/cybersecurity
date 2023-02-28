'''
Code 1
#!/usr/bin/python3
def helloworld():
    print("Hello World")
    return
helloworld()
'''

'''
Code 2
#!/usr/bin/python3
def helloworld(def_variable):
    print("Hello World "+def_variable)
    return
name=input("What is your name? ")
helloworld(name)
'''

#!/usr/bin/python3
def helloworld(variable1, variable2):
    print("Hello "+ variable1)
    print("I will call you " + variable2)
    return
name=input("What is your name? ")
nick=input("What would you like your nickname to be? ")
helloworld(name, nick)