# visuals.py
import os

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
    def supports_ansi():
        """Check if the terminal supports ANSI escape codes."""
        return os.getenv('ANSICON') is not None or os.getenv('TERM') == 'xterm' or 'COLORTERM' in os.environ
