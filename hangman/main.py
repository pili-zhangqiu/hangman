#!/usr/bin/env python # [1]
"""
This script contains utility functions to design a hangman word game.
"""
from game_variables import *

if __name__ == "__main__":
    word_to_guess = pick_random_word(set_world_list())
    
    while True:
        guess = ask_for_input()
        is_guess_in_word = check_guess(guess, word_to_guess)
    