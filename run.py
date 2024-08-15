import gspread
from google.oauth2.service_account import Credentials

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

