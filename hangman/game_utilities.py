#!/usr/bin/env python # [1]
"""
This script contains utility functions to design a hangman word game.
"""

import random
import string

from typing import List

def set_world_list() -> List[str]:
    """
    Returns a preset list of words.

    Returns
    -------
    :returns: Preset list of words.
    :rtype: List[str]
    """
    word_list = ['apple', 'banana', 'cherry', 'dragon fruit', 'pear']
    return word_list

def pick_random_word(list_to_pick_from : List[str]) -> str:
    """
    Chooses and returns a random word from the input list.
    
    Parameters
    ----------
    :param list_to_pick_from: List of strings to choose a word from.
    :type list_to_pick_from: List[str]

    Returns
    -------
    :returns: Random word from the input list.
    :rtype: str
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
    :returns: Valid letter input by user.
    :rtype: str
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
    :param guess: Letter to check
    :type guess: str
    :param word_to_guess: The word that might contain or not the letter.
    :type word_to_guess: str

    Returns
    -------
    :returns: True if the letter is in the word; False otherwise.
    :rtype: bool
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