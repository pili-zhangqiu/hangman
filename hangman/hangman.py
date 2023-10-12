import random
import string

from typing import List

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    letters : list
        List of unique letters in the word
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list : List[str], num_lives=5):
        # Initialise attributes
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.letters = set([*self.word])
        self.num_letters = len(self.letters)
        self.list_of_guesses = list()
        
        # Print initialisation messages
        print(f"The mistery word has {self.num_letters} characters")
        print(f"{self.word_guessed}")

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked
        '''
        # Convert letter to lower case
        letter = letter.lower()

        # Check if guessed letter is in the word
        if letter in self.word:
            print(f"Good guess! {letter} is in the word.")

            # Add correct letter to word_guessed
            for i in range(len(self.word)):
                if letter == self.word[i]:
                    self.word_guessed[i] = letter

            # Reduce number of unique letters not guessed by one
            self.num_letters -= 1
        
        else:
            print(f"Sorry, {letter} is not in the word.")

            # Lose a life when the letter is not in the word
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

    def ask_letter(self) -> None:
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # Ask user to input a guess
        guess = input("Enter a guess: ") 

        # Check if guess is in a valid format
        if len(guess) != 1 or guess not in string.ascii_letters:
            print("Invalid letter. Please, enter a single alphabetical character.") 

        # Check if guess was already entered
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")

        # If the guess is in a valid format and is a new guess, check and update results
        else:
            self.check_letter(guess)
            self.list_of_guesses.append(guess)


def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    is_game_ended = False

    while not is_game_ended:
        # Check if player is still alive 
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            is_game_ended = True

        # Check if the word has been guessed. If not, continue the game.
        elif game.num_letters > 0:
            game.ask_letter()
        
        # If the player is alive and there are no letters reamining to guess, then the player won
        else:
            print("Congratulations! You won!")
            is_game_ended = True


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
