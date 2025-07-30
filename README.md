WordPy - A Wordle-like Game
This repository contains a Python implementation of a word-guessing game, similar to Wordle. The game includes a bot that attempts to guess a hidden five-letter word.

Features

Game Engine: A core GameEngine class to manage the game logic.


Bot Player: An intelligent Bot that can play the game by making informed guesses.


Customizable Word List: The game uses a words.txt file as its dictionary of valid five-letter words.


Prerequisites
Python 3.x

Installation
Clone this repository to your local machine.

Ensure you have the following files in the same directory:

bot.py

GameEngine.py

letter.py

words.txt

Usage
To play a new game, you can run GameEngine.py and have the bot attempt to guess a word. The game will automatically select a random word from 

words.txt unless you specify a target_word when calling the play() method.

The 

GameEngine will provide feedback on each guess using the following format:

?: The letter is not in the word.

*: The letter is in the word but in the wrong position.

The letter itself: The letter is in the correct position.

Here is an example of how the bot would be used to play a new game:

Python

from GameEngine import GameEngine
from bot import Bot

if __name__ == "__main__":
    bot = Bot("words.txt")
    game = GameEngine()
    game.play(bot)
File Structure

bot.py: Contains the Bot class, which implements the logic for an automated player.


GameEngine.py: Contains the GameEngine class, which handles the main game loop, word selection, and feedback formatting.


letter.py: Defines the Letter class, which is used to track the status of individual letters in a guess.


words.txt: A list of five-letter words used as the dictionary for the game
