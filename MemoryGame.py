

# Properties
# 1. Difficulty
# Methods
# 1. generate_sequence - Will generate a list of random numbers between 1 to 101. The list
# length will be difficulty.
# 2. get_list_from_user - Will return a list of numbers prompted from the user. The list length
# will be in the size of difficulty.
# 3. is_list_equal - A function to compare two lists if they are equal. The function will return
# True / False.
# 4. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.
import random
import time
from Utils import screen_cleaner

def generate_sequence(difficulty):
    list_of_number = []
    i = 0
    while i < difficulty:
        list_of_number.append(random.randint(1, 100))
        i = i + 1
    return list_of_number

def get_list_from_user(difficulty):
    list_of_number = []
    i = 0
    while i < difficulty:
        list_of_number.append(int(input("Please chose number between 1 to 100: ")))
        i = i + 1
    return list_of_number

def is_list_equal(difficulty):
    generate_list = generate_sequence(difficulty)
    print(f"List of number : {generate_list}")
    time.sleep(2)
    screen_cleaner()
    guess_list_from_user = get_list_from_user(difficulty)
    if generate_list == guess_list_from_user:
        return True
    else:
        return False


def play_memo(difficulty):
    compare_results_status = is_list_equal(difficulty)
    status = False
    if compare_results_status:
        print("you win")
        status = True
    else:
        print("you lost")
    return status
