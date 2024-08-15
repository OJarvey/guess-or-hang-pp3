import os
import shutil


class Colors:
    """
    Provides ANSI escape codes for colored output.

    Attributes:
        CYAN (str): ANSI escape code for cyan color.
        RED (str): ANSI escape code for red color.
        GREEN (str): ANSI escape code for green color.
        ORANGE (str): ANSI escape code for orange color.
        BLUE (str): ANSI escape code for blue color.
        YELLOW (str): ANSI escape code for yellow color.
        PURPLE (str): ANSI escape code for purple color.
        NORMAL (str): ANSI escape code to reset color to default.
    """
    CYAN = '\033[96m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    ORANGE = '\033[1;33m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    PURPLE = '\033[95m'
    NORMAL = '\033[0m'

    @staticmethod
    def get_available_colors():
        """Returns a list of available colors."""
        return [
            Colors.CYAN,
            Colors.RED,
            Colors.GREEN,
            Colors.ORANGE,
            Colors.BLUE,
            Colors.YELLOW,
            Colors.PURPLE
        ]

    @staticmethod
    def supports_ansi():
        """Check if the terminal supports ANSI escape codes."""
        return (os.getenv('ANSICON') is not None or
                os.getenv('TERM') == 'xterm' or
                'COLORTERM' in os.environ)


HANGMAN_STAGES = [
    f"""{Colors.CYAN}
  +---+
  |   |
      |
      |
      |
      |
{Colors.NORMAL}
""",
    f"""{Colors.CYAN}
  +---+
  |   |
  O   |
      |
      |
      |
{Colors.NORMAL}
""",
    f"""{Colors.CYAN}
  +---+
  |   |
  O   |
  |   |
      |
      |
{Colors.NORMAL}
""",
    f"""{Colors.CYAN}
  +---+
  |   |
  O   |
 /|   |
      |
      |
{Colors.NORMAL}
""",
    f"""{Colors.CYAN}
  +---+
  |   |
  O   |
 /|\\ |
      |
      |
{Colors.NORMAL}
""",
    f"""{Colors.ORANGE}
  +---+
  |   |
  O   |
 /|\\ |
 /    |
      |
{Colors.NORMAL}
""",
    f"""{Colors.RED}
  +---+
  |   |
  O   |
 /|\\ |
 / \\ |
      |
{Colors.NORMAL}
"""
]


def render_hangman_graphic(attempts, level):
    """
    Renders the hangman graphic based on the current difficulty level.
    """
    valid_levels = ['easy', 'medium', 'hard']
    if not isinstance(level, str) or level not in valid_levels:
        raise ValueError(f"Invalid level: Must be one of {valid_levels}.")

    max_attempts = len(HANGMAN_STAGES) - 1

    if not (0 <= attempts <= max_attempts):
        raise ValueError(
            f"Invalid number of attempt:Must be between 0 and {max_attempts}.")

    index = attempts
    if level == 'medium':
        index = 1 + attempts
    elif level == 'hard':
        index = 2 + attempts

    if not Colors.supports_ansi():
        print(
            HANGMAN_STAGES[index].replace(Colors.CYAN, '')
            .replace(Colors.RED, '')
            .replace(Colors.ORANGE, '')
            .replace(Colors.NORMAL, '')
        )
    else:
        print(HANGMAN_STAGES[index])


def check_and_print(text):
    """
    Checks terminal size and ANSI support, and prints text accordingly.
    """
    columns, lines = shutil.get_terminal_size(fallback=(80, 20))
    if Colors.supports_ansi():
        if (len(text.splitlines()[0]) > columns or
                len(text.splitlines()) > lines):
            print("Your terminal is too small to display the full text.")
        else:
            print(text)
    else:
        print(
            text.replace(Colors.CYAN, '')
            .replace(Colors.RED, '')
            .replace(Colors.ORANGE, '')
            .replace(Colors.NORMAL, '')
        )


def display_title():
    """
    Display the title on the main menu.
    """
    title = f"""{Colors.PURPLE}
******************************************************************
*██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗*
*██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║*
*███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║*
*██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║*
*██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║*
*╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝*
******************************************************************
{Colors.NORMAL}"""

    check_and_print(title)


def display_victory():
    """
    Display the victory screen.
    """
    victory = f"""{Colors.GREEN}
*******************************************************************************
*██╗    ██╗███████╗██╗     ██╗       ██████╗  ██████╗ ███╗   ██╗███████╗██╗██╗*
*██║    ██║██╔════╝██║     ██║       ██╔══██╗██╔═══██╗████╗  ██║██╔════╝██║██║*
*██║ █╗ ██║█████╗  ██║     ██║       ██║  ██║██║   ██║██╔██╗ ██║█████╗  ██║██║*
*██║███╗██║██╔══╝  ██║     ██║       ██║  ██║██║   ██║██║╚██╗██║██╔══╝  ╚═╝╚═╝*
*╚███╔███╔╝███████╗███████╗███████╗  ██████╔╝╚██████╔╝██║ ╚████║███████╗██╗██╗*
* ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝*
*******************************************************************************

********************************************************************
*██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ██╗██████╗     ██╗████████╗*
*╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██║██╔══██╗    ██║╚══██╔══╝*
* ╚████╔╝ ██║   ██║██║   ██║    ██║  ██║██║██║  ██║    ██║   ██║   *
*  ╚██╔╝  ██║   ██║██║   ██║    ██║  ██║██║██║  ██║    ██║   ██║   *
*   ██║   ╚██████╔╝╚██████╔╝    ██████╔╝██║██████╔╝    ██║   ██║   *
*   ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝╚═════╝     ╚═╝   ╚═╝   *
********************************************************************
{Colors.NORMAL}"""

    check_and_print(victory)


def display_defeat():
    """
    Display the defeat screen.
    """
    defeat = f"""{Colors.RED}
****************************************************************************
* ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ *
*██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗*
*██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝*
*██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗*
*╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║*
* ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝*
****************************************************************************
{Colors.NORMAL}"""

    check_and_print(defeat)
