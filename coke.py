# Python_Intro
# Problem Set 2
#A series of exercises for CS50 hands-on projects
"""
This one it's my aproach on the coke machine problem
"""
Amount_due = 50
while Amount_due > 0:
    print("Amount Due: ", Amount_due)
    coin = int(input("Insert Coin: "))
   # if Coin == 25 or coin == 10 or coin == 5:
    if coin in [25, 10, 5]:
        Amount_due -= coin
