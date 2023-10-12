#!/usr/bin/env python # [1]
"""
This script contains utility functions to design a hangman word game.
"""

import random
import string

from typing import List

def get_world_list() -> List[str]:
    """
    Returns a preset list of words.

    Returns
    -------
    List[str]
        Preset list of words.
    """
    word_list = ['apple', 'banana', 'cherry', 'dragon fruit', 'pear']
    return word_list

def pick_random_word(list_to_pick_from : List[str]) -> str:
    """
    Chooses and returns a random word from the input list.
    
    Parameters
    ----------
    list_to_pick_from : List[str]
        List of strings to choose a word from.

    Returns
    -------
    str
        Random word from the input list.
    """
    word = random.choice(list_to_pick_from)
    return word

def ask_for_input() -> str:
    """
    Asks the user to input a letter guess in the terminal and 
    validates if it's a letter character (e.g. AaBbCc).
     
    If it's a valid letter, it will return the value. Otherwise,
    it will continue prompting the user to re-introduce a letter.

    Returns
    -------
    str
        Valid letter input by user.
    """
    # Ask user to input a guess
    guess = input("Enter a guess: ") 

    # As long as guess is invalid, keep asking user to input valid letter
    while len(guess) != 1 or guess not in string.ascii_letters:
        guess = input("Invalid letter! Please, enter a single alphabetical character:") 

    return guess

def check_guess(guess : str, word_to_guess : str) -> bool:
    """
    Checks whether a letter is in a given word.

    Parameters
    ----------
    guess : str
        Letter to check
    word_to_guess : str
        The word that might contain or not the letter.

    Returns
    -------
    bool
        True if the letter is in the word; False otherwise.
    """
    # Convert strings to lower case
    guess = guess.lower()
    word_to_guess = word_to_guess.lower()

    # Check if guessed letter is in the word
    if guess in word_to_guess:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False
    