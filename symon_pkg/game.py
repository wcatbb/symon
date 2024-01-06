"""
Game functions
"""
import time
from symon_pkg.controller import symon_turn, user_turn
from symon_pkg.screens import show_splash, clear_screen, show_high_scores


def new_game(USER, HIGH_SCORE, high_scores):
    '''
    prompts user for name on first try; stores symon and user sequences
    in lists and updates score for every level advanced
    '''
    symon_seq = []
    user_seq = []
    score = 0
    alive = True  # set game loop flag

    if USER == "":
        USER = input("\nEnter your name: ")
        print(f"welcome {USER}")
    print(f"\n[your best score]→ {HIGH_SCORE}")
    print("\ntype w [↑] a [←] s [↓] d [→] + 'return' to lock in your path.")
    input("press ENTER to begin")
    clear_screen()

    while alive:
        level = score + 1
        new_arrow = symon_turn()
        symon_seq.append(new_arrow)
        print(f"-=LEVEL {level}=-")
        print(f"symon's turn:{symon_seq}")
        display_time = (4 + level) / (level + 1) # shortens the amount of time user can see sequence the further they advance
        time.sleep(display_time)
        clear_screen()

        user_seq = user_turn()
        if user_seq == symon_seq:
            score += 1
            print("CORRECT!")
            time.sleep(1)
            clear_screen()
            continue
        alive = False
        clear_screen()

    if score == 1:
        print(f"\nGAME OVER! You made it {score} level deep into symon's terminal abyss...")
    else:
        print(f"\nGAME OVER! You made it {score} levels deep into symon's terminal abyss...")
        
    if score > HIGH_SCORE:
        print("...and you set a new high score!")
        HIGH_SCORE = score
        high_scores[USER] = score
        show_high_scores(high_scores)
    try_again = input("Try again? [y/n]")
    if try_again.lower() == "y":
        new_game(USER, HIGH_SCORE, high_scores)
    show_splash()
    return high_scores