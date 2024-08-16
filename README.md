# GUESS OR HANG

Welcome to GUESS OR HANG a Hangman Game!
This is a classic word-guessing game where players try to guess a hidden word by
suggesting letters within a limited number of attempts.
The game is implemented in Python and uses Google Sheets to fetch words dynamically.

![HANGMAN](readme-images/1.hangman-title.png)

Find link to game here: <https://guess-or-hang-bc6bf8f00227.herokuapp.com/>

## Table of Contents

- [About the Project](#about-the-project)
- [Game Features](#game-features)
- [Technology Used](#technology-used)
- [Installation](#installation)
- [Usage](#usage)
- [Game Instructions](#game-instructions)
- [Game Flowchart](#game-flowchart)
- [BUGS](#bugs)
- [CREDITS](#credits)

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

## Installation

### Prerequisites

- Python 3.x
- Google Cloud account with access to Google Sheets API
- Heroku CLI (for deployment)
- `creds.json`: Service account credentials for Google Sheets API

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/OJarvey/guess-or-hang-pp3.git
    cd guess-or-hang
    ```

2. **Install dependencies**:

    ```bash
    pip3 freeze > requirements.txt
    ```

3. **Set up Google Sheets API**:
   - Enable the Google Sheets API and obtain the `creds.json` file.
   - Place the `creds.json` file in the root directory of the project.

4. **Run the game locally**:

    ```bash
    python run.py
    ```

5. **Deploy to Heroku**:

    1. Log in or sign up to Heroku and create a new app.
    2. Choose a unique name for your app.
    3. In the settings tab, reveal the config vars. Then enter a key name and the value you need from the google sheets json file. Which should include the following:
    - type
    - project_id
    - private_key_id
    - private_key
    - client_email
    - client_id
    - auth_url
    - token_url
    - auth_provider_x509_cert_url
    - client_x509_cert_url
    - universe_domain

- Click add to save.

    1. Below that, click "Add buildpack," select Python, and save.
    2. Click "Add buildpack" again, this time select Node.js and save.
    3. Ensure that Python is listed above Node.js in the buildpack order.
    4. Go to the deploy tab and select GitHub as the deployment method. Connect your GitHub account.
    5. When prompted, enter the repository you want to deploy, search for it, and once found, connect it.
    6. You can choose to set it for automatic deployment or do it manually.
  - Automatic deployment will occur every time you push something to GitHub.
  - Manual deployment gives you control over when the app should be deployed, but remember to do it yourself.

***
Once the app is built, Heroku will provide a link to the live web page.

- You can access the live game via the following URL: [Guess Or Hang](https://guess-or-hang-bc6bf8f00227.herokuapp.com/)
- You can access the GitHub Repository via the following URL: [Guess or Hang Repository](https://github.com/OJarvey/guess-or-hang-pp3.git)

### Usage

Once installed, you can run the game by executing the `python3 run.py` script in the terminal.
The game will start in the terminal, and you can follow the on-screen instructions to play.

## Game Flowchart

Here’s a visual representation of the game’s flow:

![Flowchart](readme-images/3.flowchart.drawio.png)

## Game Instructions

### Home Screen

![Home](readme-images\2.hangman-homescreen.png)

### Objective

The goal of the Hangman game is to guess the hidden word by suggesting letters within a limited number of attempts.
Each incorrect guess brings the hangman closer to being fully drawn.
The game ends when the word is fully guessed, or when the hangman is completely drawn.

### How to Play

1. **Starting the Game**:
   - When the game starts, you'll be presented with a main menu.

   - You can choose from three options:
      1. Start Game: Begin a new game.
      2. How to Play: View the game instructions.
      3. Exit: Close the game.
   - To start a new game, select "Start Game" from the menu.

   ![main menu](readme-images/4.main-menu.png)

2. **Selecting Difficulty**:

   - After choosing to start the game, you'll be prompted to select a difficulty level:
      - Easy: 5 attempts allowed.
      - Medium: 3 attempts allowed.
      - Hard: 1 attempt allowed.
      - The difficulty level affects how many incorrect guesses you can make before the game ends.

   ![Difficulty](readme-images/5.difficulty-menu.png)

3. **Making a Guess**:
   - The game will display a series of underscores ["_"], each representing a letter in the hidden word.

   ![Underscore and Attemps](readme-images/14.underscore-with-attemps-left.png)

   - You need to guess the letters of the word one at a time:
      - Correct Guess: If the guessed letter is in the word, it will be revealed in all the correct positions.

   ![Correct Guess](readme-images/7.corrected-guess-screen.png)

      - Incorrect Guess: If the guessed letter is not in the word,
      one part of the hangman will be drawn, and you lose one attempt.

      ![Incerrect Guess](readme-images/8.wrong-guess-screen.png)

      - You can also attempt to guess the entire word at once,
   but be careful, if your guess is wrong, it counts as an incorrect attempt.

4. **Using Hints**:
   - If you're stuck, you can type 'hint' to reveal one of the hidden letters in the word.
   - Using a hint will cost you one attempt, so use it wisely.
   - Hints are only available if you have more than one attempt left.

5. **Winning the Game**:
   - You win the game by guessing all the letters in the word correctly before running out of attempts.
   - When you win, a victory screen will be displayed, congratulating you on your success and asking if you want to play again.

   ![Winning](readme-images/15.winning-screen.png)

6. **Losing the Game**:
   - If you run out of attempts before guessing the word, the game ends, and the hangman is fully drawn.
   - A defeat screen will be displayed, showing the correct word and asking if you want to play.

   ![Game Over](readme-images/13.game-over.png)

7. Replaying the Game:

   - After the game ends, whether you win or lose, you will be asked if you want to play again.
   - Type y to start a new game or n to exit.

   ![Replay](readme-images/16.play-again.png)

8. Exiting the Game:

   - You can exit the game at any time by selecting "Exit" from the main menu or by choosing not to replay after a game ends.

## BUGS

### CREDITS
