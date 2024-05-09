import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES, CODE_LEN = 10, 4

def gen_code() :
    code = []
    
    for _ in range(CODE_LEN) :
        color = random.choice(COLORS)
        code.append(color)
        
    return code

def guess_code() :
    
    while True :
        guess = input("Guess: ").upper().split(" ")
        
        if len(guess) != CODE_LEN :
            print(f"You must guess {CODE_LEN} colors.")
            continue
        
        for color in guess :
            if color not in COLORS :
                print(f"Invalid color: {color}. Try again. ")
                break
            else :
                break
        
    return guess

def check_code(guess, real_code) :
    count, correct_pos, incorrect_pos = {}, 0, 0
    
    for color in real_code :
        if color not in count :
            count[color] = 0
            
        count[color] += 1
        
    for guess_color, real_color in zip(guess, real_code) :
        if guess_color == real_color :
            correct_pos += 1
            count[guess_color] -= 1
            
    for guess_color, real_color in zip(guess, real_code) :
        if guess_color in count and count[guess_color] > 0:
            incorrect_pos += 1
            count[guess_color] -= 1
            
    return correct_pos, incorrect_pos

def game() :
    print(f"Welcome to Chromatic Conundrum, you have {TRIES} to guess the correct color code...")
    print(f"The Valid colors are", *COLORS)
    
    code = gen_code()
    for attempts in range(1, TRIES + 1) :
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LEN :
            print(f"You guessed the code in {attempts} tries!")
            break
        
        print(f"Correct positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
        
    else :
        print("Sorry, ran out of tries!, the code was:", *code)
        
if __name__ == "__main__" :
    game()