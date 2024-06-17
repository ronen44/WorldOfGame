# A package that is in charge of managing the scores file.
# The scores file at this point will consist of only a number. That number is the accumulation of the
# winnings of the user. Amount of points for winning a game is as follows:
# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
# Each time the user is winning a game, the points he one will be added to his current amount of
# point saved in a file.

# add_score - The function’s input is a variable called difficulty. The function will try to read
# the current score in the scores file, if it fails it will create a new one and will use it to save
# the current score.


from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    points_of_winning = difficulty * 3 + 5
    fr = open(SCORES_FILE_NAME, 'r')
    file_score = fr.read()
    fr.close()

    if not file_score:
        file_score = 0

    new_score = int(file_score) + points_of_winning
    new_score_w = str(new_score)
    #print(f"your new score is : {new_score}")
    fw = open(SCORES_FILE_NAME, 'w')
    fw.write(new_score_w)
    fw.close()
    

def read_score():
    try:
        fr = open(SCORES_FILE_NAME, 'r')
        file_score = fr.read()
        # new_score_w = file_score
        fr.close()
    except:
        file_score = "file not found"
    return file_score

