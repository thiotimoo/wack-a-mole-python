import random
import time
import os
import shelve


        
def main():
    main_menu();

def get_highscore():
    highscore = 0
    try:
        d = shelve.open('score.txt')
        highscore = d.get('score', 0)
        d.close()
    except FileNotFoundError:
        highscore = 0
    return highscore

def main_menu():
    clear_terminal()
    highscore = get_highscore()
    welcome_message = "WACK_A_MOLE.py"    
    print("====================")
    print(f"== {welcome_message} ==")
    print("====================")
    print(f"   HIGHSCORE: {highscore}")
    
    generate_menu([
        {"label": "START GAME", "callback": start_game},
        {"label": "EXIT GAME", "callback": exit_game},
    ])

def generate_menu(items):
    print("====================")
    for i, item in enumerate(items):
        print(f"{str(i + 1)}) {str(item["label"])}")
    print("====================")
    
    valid = False
    while (not valid):
        selected = input("SELECT: ")
        selected = int(selected)
        if (selected >= 1 and selected <= len(items)):
            valid = True
            items[selected - 1].get("callback")()
            break;
        else:
            print("Invalid Input! Try again.")

def start_game():
    score = 0
    life = 3
    total_life = 3
    while (life > 0):
        mole_position = random.randint(1,4);
        wacked = False
        while not wacked:
            clear_terminal();
            life_str = ""
            for l in range(total_life):
                if (l < life):
                    life_str += "❤️ "
            print(life_str)
            print(f"Score: {score}")
            print("====================")
            if (life <= 0):
                break;
            
            
            print('🕳️ 🕳️ 🕳️ 🕳️ 🕳️')
            print('1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣')
            print("====================")
            guess = input("Where do you think the mole is? ")
            wacked = True
            if (guess == str(mole_position)):
                print('WOW, You wacked a mole! 👍')
                score += 1
            else:
                print('You missed the mole, try again! 💔')
                life -= 1
            time.sleep(2)
        if (life <= 0):
            print('You lost! The mole ruined your garden. 😢')
            time.sleep(2)
            highscore = get_highscore()
            if (int(score) > int(highscore)):
                d = shelve.open('score.txt')
                highscore = score
                d['score'] = highscore
                d.close()
                print(f'New highscore! {highscore} points. ✨')
            else:
                print(f'Your score is {score}, and your highscore is {highscore}')
            time.sleep(2)
            return main();
        
def clear_terminal():
    os.system('cls||clear')

def exit_game():
    exit();
    
main()