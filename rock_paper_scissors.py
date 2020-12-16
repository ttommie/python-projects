#------------------#
# ┌┬┐┌─┐┌┬┐┌┬┐┬┌─┐ #
#  │ │ ││││││││├┤  #
#  ┴ └─┘┴ ┴┴ ┴┴└─┘ #
#------------------#

# FILE: ROCK_PAPER_SCISSORS.PY
# DATE: 11/30/2020

# IMPORTS
import random
import os

# VARIABLE
player_wins = 0
computer_wins = 0
game_list = ['Rock', 'Paper', 'Scissors']
computer = game_list[random.randint(0, 2)]
player = False

while player == False:
    # SET PLAYER TO TRUE
    player = input('Rock, Paper, or Scissors? \n')
    if player.upper() == computer.upper():
        print('Tie!')
    elif player.upper() == 'ROCK':
        if computer.upper() == 'PAPER':
            print('You Lose!', computer, 'Covers', player)
            computer_wins += 1
        else:
            print('You Win!', player, 'Smashed', computer)
            player_wins += 1
    elif player.upper() == 'PAPER':
        if computer.upper() == 'SCISSORS':
            print('You Lose!', computer, 'Cuts', player)
            computer_wins += 1
        else:
            print('You Win!', player, 'Covers', computer)
            player_wins += 1
    elif player.upper() == 'SCISSORS':
        if computer.upper() == 'ROCK':
            print('You Lose!', computer, 'Smashes', player)
            computer_wins += 1
        else:
            print('You Win!', player, 'Cuts', computer)
            player_wins += 1
    else:
        print("That's not a valid play. Check your spelling!")

    # PLAYER WE SET TO TRUE | SET BACK TO FALSE SO WE CAN LOOP PLAYING
    again = input('Play Again Y/N:')

    if again.upper() == 'Y':
        player = False
        computer = game_list[random.randint(0, 2)]
    elif again.upper() == 'N':
        os.system('cls')
        print('+-------------------------------------+')
        print('Player Score: ', player_wins)
        print('Computer Score: ', computer_wins)
        if player_wins > computer_wins:
            print('Winner, Congrats! Thanks For Playing')
        elif computer_wins > player_wins:
            print('Sorry, You Lost. Thanks For Playing!')
        else:
            print('It was a Tie, Thanks For Playing!')
        print('+-------------------------------------+')
