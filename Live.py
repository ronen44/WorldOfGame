def welcome(name):
    message = (f"hello {name} and welcom to world of game (WoG).\nhear you can find many coll gamse to play.")
    return (message)

def load_game(message,lowOption, higeOption, option):
    print(message)
    number = int(input(f"Enter your chose {lowOption}-{higeOption}: "))
    while lowOption < number > higeOption:
        print(f'You chose {option} : {number}')
        number = int(input(f"Enter your chose {lowOption}-{higeOption}: "))
        print(message)
    return number
