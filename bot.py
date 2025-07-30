# Create the implementation of the Bot class here
import random
from typing import List, Optional
from GameEngine import GameEngine
from letter import Letter

word_list_file = "C:\Users\maxmo\Desktop\python-scripts\wordPY\words.txt"

class Bot:
    
    def __init__(self, word_list_file:  str) -> None:
        with open(word_list_file, 'r') as file:
            self.word_list = [word.strip().upper() for word in file]
        self.name = "Bot1"
        self.known_letters = [None, None, None, None, None]
        self.guessed_letters = []
        self.available_letters = []
            
    def make_guess(self) -> str:
        #filer known/not known letters
        filtered_word_list = []
        for word in self.word_list:
            switch = True
            for i, known_letter in enumerate(self.known_letters):
                if known_letter and word[i] != known_letter:
                    switch = False
                    break
                for letter in self.available_letters:
                    if letter in word:
                        switch = False
                        break     
            if switch:
                filtered_word_list.append(word)
        if not filtered_word_list:
            return random.choice(self.wordlist)
        guess = random.choice(filtered_word_list)
        self.guessed_letters.append(guess)
        return guess

    def record_guess_results(self, guess: str, results: list[Letter]) -> None:
        for i, letter_obj in enumerate(results):
            if letter_obj.is_in_correct_place():
                self.known_letters[i] = letter_obj.letter
            if not letter_obj.is_in_word():
                self.available_letters.append(letter_obj.letter)

b = Bot(word_list_file)
with open(word_list_file, 'r') as file:
    random_word_list = [i.strip().upper() for i in file]
    random_word = random.choice(random_word_list)

GameEngine().play(b, word_list_file=word_list_file, target_word=random_word)