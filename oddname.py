"""Sable Ching"""

while True:
    name = str(input("Please enter your name: \n"))
    if name == '':
        print("Invalid, please enter your name.")
    else:
        print(name[1::2])
        break