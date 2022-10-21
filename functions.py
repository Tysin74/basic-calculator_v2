# Creating functions to be imported into calc.py
# input_list = list(map(int, input("Type your equation: ").split())) -- Use this to take multiple inputs and stuff in an array

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

def getInput():
    input_list = list(map(str, input("Type your equation: ").split()))
    return input_list