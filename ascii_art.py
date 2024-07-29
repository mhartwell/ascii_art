import pyfiglet
from termcolor import colored

msg = input('What would you like to print?')
color = input('What color?')

ascii_art = pyfiglet.figlet_format(msg)
try:
    colored_ascii = colored(ascii_art, color=color)
except KeyError:
    colored_ascii = colored(ascii_art, color='cyan')

print(colored_ascii)
