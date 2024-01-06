'''
input controller
'''
import random
from symon_pkg.screens import clear_screen

def symon_turn():
    arrow_keys = ["UP", "DOWN", "LEFT", "RIGHT"]
    return random.choice(arrow_keys)

def user_turn():
    # Init user_seq
    user_seq = []
    print("")
    # Get arrow key input
    while True:
        key = input()
        if key == "w":
            print("↑")
            user_seq.append("UP")
        elif key == "s":
            print("↓")
            user_seq.append("DOWN")
        elif key == "a":
            print("←")
            user_seq.append("LEFT")
        elif key == "d":
            print("→")
            user_seq.append("RIGHT")
        elif key == "":
            clear_screen()
            break  # Exit the loop when the user submits the sequence

    return user_seq