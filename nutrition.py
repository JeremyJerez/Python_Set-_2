# Python_Intro
# Problem Set 2
#A series of exercises for CS50 hands-on projects
"""
This one it's my aproach on the "nutrition facts" problem
"""
#we are going to need a dict
fruits = {
    "apple" : 130,
    "avocado" : 50,
    "sweet cherries" : 100,
}   #I didn't complete the list as it isn't necessary for the tests

fruit = input("item: ")
for x in fruits:
    if x in fruit.lower():
        print("calories", fruits[x])
