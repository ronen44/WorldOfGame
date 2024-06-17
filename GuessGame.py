# 1. generate_number - Will generate number between 1 to difficulty and save it to
# secret_number.
# 2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
# return the number.
# 3. compare_results - Will compare the  secret generated number to the one prompted
# by the get_guess_from_user.
# play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.
import random

def generate_number(messge,difficulty):
    number = random.randint(1, difficulty)
    print(f"{messge} {number}")
    return number

def get_guess_from_user(message):
    number = int(input(message))
    return number


def compare_results(difficulty):
    message = f"Please chose number between 1 to {difficulty}: "
    guess_number_from_user = get_guess_from_user(message)
    secret_number_messge = "Secret number :"
    generate_number_ret = generate_number(secret_number_messge, difficulty)
    if generate_number_ret == guess_number_from_user:
        return True
    else:
        return False

def play_guess(difficulty):
    compare_results_status = compare_results(difficulty)
    status = False
    if compare_results_status:
        print("you win")
        status = True
    else:
        print("you lost")
    return status
