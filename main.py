from colorama import Fore, Back, Style, init
init(autoreset=True)

class Styles:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

BLACK = Fore.BLACK
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE

BG_BLACK = Back.BLACK
BG_RED = Back.RED
BG_GREEN = Back.GREEN
BG_YELLOW = Back.YELLOW
BG_BLUE = Back.BLUE
BG_MAGENTA = Back.MAGENTA
BG_CYAN = Back.CYAN
BG_WHITE = Back.WHITE

""" Outside of print function """

print(BLACK + 'Black text color')
print(RED + 'Red text color')
print(GREEN + 'Green text color')
print(YELLOW + 'Yellow text color')
print(BLUE + 'Blue text color')
print(MAGENTA + 'Magenta text color')
print(CYAN + 'Cyan text color')
print(WHITE + 'White text color')

print(BG_BLACK + 'Black background color')
print(BG_RED + 'Red background color')
print(BG_GREEN + 'Green background color')
print(BG_YELLOW + 'Yellow background color')
print(BG_BLUE + 'Blue background color')
print(BG_MAGENTA + 'Magenta background color')
print(BG_CYAN + 'Cyan background color')
print(BG_WHITE + 'White background color')

""" Inside print function """

# Foreground colors
print(Fore.BLACK + 'Black color')
print(Fore.RED + 'Red color')
print(Fore.GREEN + 'Green color')
print(Fore.YELLOW + 'Yellow color')
print(Fore.BLUE + 'Blue color')
print(Fore.MAGENTA + 'Magenta color')
print(Fore.CYAN + 'Cyan color')
print(Fore.WHITE + 'White color')

# Background colors
print(Back.BLACK + 'Black background color')
print(Back.RED + 'Red background color')
print(Back.GREEN + 'Green background color')
print(Back.YELLOW + 'Yellow background color')
print(Back.BLUE + 'Blue background color')
print(Back.MAGENTA + 'Magenta background color')
print(Back.CYAN + 'Cyan background color')
print(Back.WHITE + 'White background color')

# Style
print(Styles.UNDERLINE + Styles.BOLD + 'Hello, World!' + Styles.END)