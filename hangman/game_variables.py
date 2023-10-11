"""
WIP: This file is used to test the creation of variables for the game.
"""
import random
import string

# Task 1: Define list of possible words
word_list = ['apple', 'banana', 'cherry', 'dragon fruit', 'pear']
print(word_list)

# Task 2: Choose a random word from the list
word = random.choice(word_list)
print(word)

# Task 3: Ask the user for an input
guess = input("Enter a guess (i.e. letter): ") 

# Task 4: Check that the input is a single letter character
while len(guess) != 1 or guess not in string.ascii_letters:
    guess = input("Invalid input! Please, enter a single letter:") 

print(f"Good guess! You've chosen: {guess}")