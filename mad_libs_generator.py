#------------------#
# ┌┬┐┌─┐┌┬┐┌┬┐┬┌─┐ #
#  │ │ ││││││││├┤  #
#  ┴ └─┘┴ ┴┴ ┴┴└─┘ #
#------------------#

# FILE: MAD_LIBS_GENERATOR.PY
# DATE: 12/16/2020

#IMPORTS
import os 

#INPUTS
again = 'Y'

while again.upper() == 'Y':
    noun_one = input('Pick a Thing: ')
    noun_two = input('Pick a Place: ')
    name_one = input('Pick a Name: ')
    name_two = input('Pick a Second Name: ')
    noun_three = input('Pick a Second Thing: ')
    emotion_one = input('Pick an Emotion: ')
    input('Press Enter to Generate Mad Lib...')
    print('|---------------------------------------|')
    print('The first Fire was created by {}. in a {}'.format(noun_one, noun_two))
    print('His name was {} and he was married to {}.'.format(name_one, name_two))
    print('They had 4 {} and lived {} ever after.'.format(noun_three, emotion_one))
    print('|---------------------------------------|')
    again = input('Would you Like to Try with Different Words (Y/N): ')

if again.upper() == 'N':
    os.system('cls')
    print('Thanks for Playing!')
