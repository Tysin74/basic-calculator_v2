from functions import *

while True:
    eq_list = getInput()

    for i in range(0, len(eq_list)):
            if eq_list[i].lstrip('-').isdigit():
                eq_list[i] = int(eq_list[i])
                print(eq_list[i], "is now a", type(eq_list[i]))
            else:
                print(eq_list[i], "is still a string.")

    for i in range(0, len(eq_list)):
        print(eq_list[i], "is still a", type(eq_list[i]))