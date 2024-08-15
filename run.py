import random
import gspread
from google.oauth2.service_account import Credentials
from visuals import (
        display_title, 
        display_victory, 
        display_defeat, 
        render_hangman_graphic, 
        Colors
)

# Constants
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Google Sheets API Setup
CREDENTIALS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDENTIALS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('guess-or-hang')

# Utility Functions
def fetch_word() -> str:
    """Fetches a random word from Google Sheets."""
    try:
        sheet = GSPREAD_CLIENT.open('guess-or-hang').sheet1
        word_list = sheet.col_values(1)
        if not word_list:
            raise ValueError("Word list is empty. Please add words to the spreadsheet.")
        return random.choice(word_list).lower()
    except gspread.exceptions.APIError as e:
        raise ValueError(f"Error accessing Google Sheets: {e}")
    except gspread.exceptions.SpreadsheetNotFound as e:
        raise ValueError(f"Spreadsheet 'guess-or-hang' not found: {e}")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")
    
def provide_hint(word: str, guesses: list, max_attempts: int, attempts_left: int) -> tuple:
    """Provides a hint by revealing a random unguessed letter."""
    if attempts_left <= 1:
        print(f"{Colors.RED}No hints available!{Colors.NORMAL}")
        return guesses, attempts_left
    
    unguessed_indices = [i for i, char in enumerate(guesses) if char == '_']
    if not unguessed_indices:
        print(f"{Colors.RED}No more hints can be provided!{Colors.NORMAL}")
        return guesses, attempts_left
    
    hint_index = random.choice(unguessed_indices)
    guesses[hint_index] = word[hint_index]
    attempts_left -= 1
    print(f"{Colors.GREEN}Hint used! Remaining attempts: {attempts_left}{Colors.NORMAL}")

    return guesses, attempts_left

def request_replay() -> bool:
    """Asks the player if they would like to play another round."""
    while True:
        choice = input(f"{Colors.PURPLE}Play again? (y/n): {Colors.NORMAL}").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        else:
            print(f"{Colors.RED}Invalid input. Please enter 'y' or 'n'.{Colors.NORMAL}")
