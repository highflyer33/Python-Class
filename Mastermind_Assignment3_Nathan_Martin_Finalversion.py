### Block comment goes here
# Nathan Martin
# October 7, 2022
#This is a game called Mastermind, you get 5 tries to gues the right color combination out of 8 different colored pegs.
#The game must contain error messages if colors are repeated, more or less than 4 choices in the guess, and if the guessed color is not in the available list.

from enum import Flag
from typing import Counter

legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']


def generate_color_sequence():
    import random
    random.seed()

    sequence = random.sample(range(len(legal_colors)), 4)
    return [legal_colors[i] for i in sequence]

colors = generate_color_sequence()

#print function to explain game to player.

print("In this game you will guess which 4 colored pegs are chosen by a randomizer. There are eight colored pegs R, G, B, Y, W, O, M, V. \nInput your guess with no spaces between colors. Peg colors cannot be repeated. \nW means you have guessed the rigth color but it is in the wrong place. \nR means you have guessed the right color and place. \n_ means that the guessed color is not in the chosen list. ")
Tries = 1
win = False
legal = False
while Tries  <= 5:
#Guess
    guess=input(f"Guess {Tries}:")
    guess = guess.upper()
    #for loop to see if guess has duplicates    
    for color in guess:
        if guess.count(color) > 1:
            print("Colors cannot be repeated, try again")
            break
    #if loop using length of guess to detmine through boolean question if the guess is the required 4 characters and rejects if not.      
    if(len(guess) != 4):
        print("Must be 4 colors, try again.")
        continue

    legal = True

    for color in guess:
        if color not in legal_colors:
                print(f"{color} is not in available list, try again.")
                legal = False
    if not legal:
        continue

    Tries += 1    
    #Check if guess is correct, skip to print function "You win."
    if list(guess) == colors:
        win = True
        break
    
    #Check if color is maching position of guess color or if it is simply present within the index but in another place.
    peg = ""
    for index in range(len(guess)):
        if guess[index] == colors[index]:
            peg = peg+ "R" #Adds R if correct place and peg.
        elif guess[index] in colors: 
            peg = peg+ "W" #Adds W if correct peg but incorrect place.
        else:
            peg = peg+ "_" #Adds _ if incorrect peg and place.
    #Combine string together for peg hint answer.        
    print(peg)
            
    
#Print for "You win" if list(guess) == colors, ends program after printing "You win."
if win:
        print("You win")
#Print for "You lose" if list(guess) != colors, loops through 5 guesses then terminates.            
else:
    print("You lose.")