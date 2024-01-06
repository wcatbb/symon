'''
input controller
'''
import random
from symon_pkg.screens import clear_screen

def symon_turn():
    '''
    returns random arrow direction from list
    '''
    arrow_keys = ["UP", "DOWN", "LEFT", "RIGHT"]
    return random.choice(arrow_keys)

def user_turn():
    '''
    user sequence stores a list of key inputs which is returned
    when the input loop is exited  
    '''
    user_seq = []
    print("")
    # get arrow key input
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
            break  # exit the loop when the user hits return
    return user_seq