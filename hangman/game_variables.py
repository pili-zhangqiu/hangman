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

def request_user_guess() -> str:
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
    guess = input("Enter a guess (i.e. letter): ") 

    # As long as guess is invalid, keep asking user to input valid letter
    while len(guess) != 1 or guess not in string.ascii_letters:
        guess = input("Invalid input! Please, enter a single letter:") 

    return guess