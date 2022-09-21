from sys import exit
from random import choice


def Intro_to_game():
    print ("\nWelcome to best Rock, Paper, Scissors game out there.\n")
    print ("Do you want to play\n")

    continue_playing = input("'Yes' to continue, 'No' to exit the game >  ")

    if continue_playing == 'No' or continue_playing == 'no':
        exit()

    elif continue_playing == 'Yes' or continue_playing == 'yes':
        print("\nWonderfull. Now I will ask if you either want Rock, Paper, or ")
        print("Scissors and I will tell you how you did. Best of three, wins!")

    else:
        print("\nInvalid input, type 'Yes' or 'No' please.")
        Intro_to_game()


def Combat():
    your_score = 0
    program_score = 0
    chances_left = 0

    while chances_left != 3 and your_score != 2 and program_score != 2:

        your_hand = input("Choose your weapon!!! > ")

        if your_hand == 'Paper' and rock_paper_scissors != 'Scissors':
            print("\nGod dammit you got me!!!")
            your_score += 1
            print ("Your score: {}".format(your_score))

        elif your_hand == 'Rock' and rock_paper_scissors != 'Paper':
            print("\nWhatever, it's really stupid that a piece of paper defeats a rock  <_<")
            your_score += 1
            print ("Your score: {}".format(your_score))

        elif your_hand == 'Scissors' and rock_paper_scissors != 'Rock':
            print("\nHey!, watch out, that thing is sharp!! O_O")
            your_score += 1
            print ("Your score: {}".format(your_score))

        else:
            print("\nHa!, take that tough guy. <~<")
            program_score += 1
            print ("Program Score: {}".format(program_score) )

    if program_score == 2:
        print("\nYay!!!, I win ^~^ . Try next time!")

    elif your_score == 2:
        print("\nDamm!!, you win A_A . Open again any time you wanna play, ok? :)")

    else:
        print("Something went wrong haha!")




Intro_to_game()

print("\nWe beggin, Good Luck!\n")

rock_paper_scissors = choice(['Rock', 'Paper', 'Scissors'])

Combat()
