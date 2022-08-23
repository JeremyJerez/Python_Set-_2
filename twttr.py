# Python_Intro
# Problem Set 2
#A series of exercises for CS50 hands-on projects
"""
This one it's my aproach on the "Just setting up my twttr" problem
"""
x = input("Input: ")

print("Output: ", end="")
for letter in x:
    if not letter.lower() in ["a", "e", "i", "o", "u"]:
        print(letter, end="")
print()
