# GUESS OR HANG

Welcome to GUESS OR HANG a Hangman Game!
This is a classic word-guessing game where players try to guess a hidden word by suggesting letters within a limited number of attempts.
The game is implemented in Python and uses Google Sheets to fetch words dynamically.

![HANGMAN](readme-images/1.hangman-title.png)

Find link to game here: <https://guess-or-hang-bc6bf8f00227.herokuapp.com/>

## Table of Contents

- [About the Project](#about-the-project)
- [Game Features](#game-features)
- [Technology Used](#technology-used)

## About the Project

This Hangman game was developed as an educational project to demonstrate the use of Python for game development,
including the integration with Google Sheets for dynamic word selection. The game features colorful terminal output,
providing a fun and interactive way to play the classic game of Hangman.

## Game Features

- **Dynamic Word Fetching**: Words are fetched from a Google Sheet, allowing for easy updates and changes to the word list.
- **Difficulty Levels**: Three difficulty levels (Easy, Medium, Hard) with varying numbers of allowed incorrect attempts.
- **Hints**: Players can request hints, which reveal a letter in the word at the cost of an attempt,
players must read the instructions to understand how to use the 'hint'.
- **Colorful Output**: The game uses ANSI escape codes to color the terminal output, enhancing the visual experience.
- **Victory and Defeat Screens**: Custom victory and defeat screens are displayed based on the game outcome.

## Technology Used

- **Python**: The core language used to develop the game.
- **Google Sheets API**: Used to fetch words dynamically from a Google Sheet.
- **Colorama**: A Python library used for cross-platform colored terminal text.
- **Heroku**: Deployment platform used for running the game in a live environment.
