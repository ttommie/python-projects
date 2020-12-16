#------------------#
# ┌┬┐┌─┐┌┬┐┌┬┐┬┌─┐ #
#  │ │ ││││││││├┤  #
#  ┴ └─┘┴ ┴┴ ┴┴└─┘ #
#------------------#

# FILE: NUMBER_GUESSING_GAME.PY
# DATE: 12/15/2020

# IMPORTS
import random
import os 

#INPUTS
guess_count = 0
again = 'Y'

while again.upper() == "Y":
    input_value = int(input('Guess a Number: '))
    guess_count += 1
    rand_num = random.randint(1, 10)
    if input_value == rand_num:
        print('The Number Was :', rand_num)
        print('You got it Correct!')
        print('Guesses: ', guess_count)
    elif input_value != rand_num:
        print('The Number was :', rand_num)
        print('You Got it Incorrect.')
    again = input('Would you Like to Play Again (Y/N): ')

if again.upper() == "N":
    os.system('cls')
    print('Thanks for playing!')

