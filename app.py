'''
Portfolio Project: symon
By Doug Beatty
1.5.24

symon is a memory game that follows the mechanics of
the popular 80s handheld game Simon. Where Simon uses
color sequences, symon uses random arrow sequences
that the user must repeat.

logo attr: Text to ASCII Art Generator (TAAG) [https://patorjk.com/]
'''

from symon_pkg.screens import show_splash, show_high_scores, show_rules
from symon_pkg.game import new_game

# global definitions
USER = ""
HIGH_SCORE = 0
high_scores = {
    "dante": 8,
    "bug": 7,
    "koko": 6,
    "prince": 5,
    "bella": 4,
    "mac": 3,
    "pelli": 2,
    "charlie": 1
}

show_splash()

# main application loop
while True:
    menu_selection = input("\n")
    if menu_selection == "1":
        new_game(USER, HIGH_SCORE, high_scores)
    if menu_selection == "2":
        show_high_scores(high_scores)
    if menu_selection == "3":
        show_rules()
    if menu_selection == "4":
        break
