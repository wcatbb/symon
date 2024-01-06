'''
Screen functions
'''
import os

def show_splash():
    '''
    main menu screen
    '''                                                                                 
    print("                                                           8 8888                           ")
    print("                                                           8 8888                           ")
    print("                                                           8 8888                           ")
    print("                                                           8 8888                           ")
    print("                                                           8 8888                           ")
    print("                                                           8 8888                           ")
    print("                                     .         .           8 8888                           ")
    print("   d888888o.  `8.`8888.      ,8'    ,8.       ,8.           ,o888888o.     b.             8 ")
    print(" .`8888:' `88. `8.`8888.    ,8'    ,888.     ,888.       . 8888     `88.   888o.          8 ")
    print(" 8.`8888.   Y8  `8.`8888.  ,8'    .`8888.   .`8888.     ,8 8888       `8b  Y88888o.       8 ")
    print(" `8.`8888.       `8.`8888.,8'    ,8.`8888. ,8.`8888.    88 8888        `8b .`Y888888o.    8 ")
    print("  `8.`8888.       `8.`88888'    ,8'8.`8888,8^8.`8888.   88 8888         88 8o. `Y888888o. 8 ")
    print("   `8.`8888.       `8. 8888    ,8' `8.`8888' `8.`8888.  88 8888         88 8`Y8o. `Y88888o8 ")
    print("    `8.`8888.       `8 8888   ,8'   `8.`88'   `8.`8888. 88 8888        ,8P 8   `Y8o. `Y8888 ")
    print("8b   `8.`8888.       8 8888  ,8'     `8.`'     `8.`8888.`8 8888       ,8P  8      `Y8o. `Y8 ")
    print("`8b.  ;8.`8888       8 8888 ,8'       `8        `8.`8888.` 8888     ,88'   8         `Y8o.` ")
    print(" `Y8888P ,88P'       8 8888,8'         `         `8.`8888.  `8888888P'     8            `Yo ")
    print("                                                  `8.`888b           ,8'                    ")
    print("                                                   `8.`888b         ,8'                     ")
    print("                                                    `8.`888b       ,8'                      ")
    print("                                                     `8.`888b     ,8'                       ")
    print("    1. New Game                                       `8.`888b   ,8'                        ")
    print("    2. Show High Scores                                `8.`888b ,8'                         ")
    print("    3. Rules                                            `8.`888b8'                          ")
    print("    4. Exit                                              `8.`888'                           ")
    print("                                                          `8.`8'                            ")
    print("                                                           `8.`                             ")

def show_high_scores(high_scores):
    '''
    leaderboard
    '''
    sorted_high_scores = sorted(high_scores.items(), key=lambda item: item[1], reverse=True)[:8]
    high_scores = dict(sorted_high_scores)
    
    print("\n   -=HIGH SCORES=-  ")
    print("↑→→→→→→→→→→→→→→→→→→↓")
    for user, high_score in high_scores.items():
        print(f"↑ {user:<12}  {high_score:<3}↓") # f-string formatting for uniform columns 
    print("↑←←←←←←←←←←←←←←←←←←↓")

def show_rules():
    '''
    the devilish circumstances
    '''
    print("\n")
    print("↑→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→↓")
    print("↑ symon is a demon that resides in your terminal  ↓")
    print("↑ you must follow its commands or else...         ↓")
    print("↑ (☹ you won't get a high score ☹)                ↓")
    print("↑                                                 ↓")
    print("↑ press your arrow keys like symon says.          ↓")
    print("↑ if you make a mistake, the game is over and     ↓")
    print("↑ symon returns to the darkest depths of the      ↓")
    print("↑ terminal until summoned again with a new game!  ↓")
    print("↑                                                 ↓")
    print("↑ how far down the terminal will you go?          ↓")
    print("↑←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←↓")

def clear_screen():
    '''
     clear the screen based on OS
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
