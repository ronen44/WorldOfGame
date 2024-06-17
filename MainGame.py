from Live import welcome , load_game
from GuessGame import play_guess
from MemoryGame import play_memo
from CurrencyRouletteGame import play_currency
from Score import add_score
from Utils import screen_cleaner

choseGameMessage = ("0.Exit and Shutdown.\n"
                "1.Memory Game – a sequence of numbers will appear for one second and you have to guess it back.\n"
               "2.Guess Game – guess number and see if you chose like as the computer.\n"
               "3.Currency Roulette – try to guess the value of a random amount of UDS in ILS.\n")

choseDifficultyMessage = ("0. back to main menu.\n"
               "1. low difficulty.\n"
               "2. medium low difficulty.\n"
               "3. medium difficulty.\n"
               "4. medium high difficulty.\n"
               "5. high difficulty.\n")

name = input("Enter your name : ")
print(welcome(name))
gameNumber = load_game(choseGameMessage,0,3, "game")
while gameNumber:
    if gameNumber == 1:
        gameDifficulty = load_game(choseDifficultyMessage, 0, 5, "difficulty")
        while gameDifficulty:
            if play_memo(gameDifficulty):
                add_score(gameDifficulty)
            gameDifficulty = load_game(choseDifficultyMessage, 0, 5, "difficulty")
    elif gameNumber == 2:
        gameDifficulty = load_game(choseDifficultyMessage, 0, 5, "difficulty")
        while gameDifficulty:
            if play_guess(gameDifficulty):
                add_score(gameDifficulty)
            gameDifficulty = load_game(choseDifficultyMessage, 0, 5, "difficulty")
    elif gameNumber == 3:
        gameDifficulty = load_game(choseDifficultyMessage, 0, 5, "difficulty")
        while gameDifficulty:
            if play_currency(gameDifficulty):
                add_score(gameDifficulty)
            gameDifficulty = load_game(choseDifficultyMessage, 0, 5, "difficulty")
    gameNumber = load_game(choseGameMessage,0,3, "game")