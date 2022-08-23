# Python_Intro
# Problem Set 2
#A series of exercises for CS50 hands-on projects
"""
This one it's my aproach on the making faces problem
"""
x = input("camel case: ")
print("snake_case: ", end="")
for i in x:
    if i.isupper():
        print("_" + i.lower(), end="")
    else:
        print(i, end="")
print()
