# madlib game.

import random

import madlib1 as m1
import madlib2 as m2
import madlib3 as m3

user_choice = input("Welcome to the Madlib game! Do you want to start? If yes, type 'y'. To exit, press any other key ")

while user_choice == 'y':
    chosen = random.randint(0, 2)  # to choose which madlib game will be played.
    if chosen == 0:
        m1.madlib()
    elif chosen == 1:
        m2.madlib()
    else:
        m3.madlib()

    user_choice = input("Do you want to play again? if yes, type 'y', if no, press any other key ")
