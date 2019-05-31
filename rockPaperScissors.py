
import random

pl_wins_rock = 0
pl_wins_paper = 0
pl_wins_scissors = 0

comp_wins_paper = 0
comp_wins_rock = 0
comp_wins_scissors = 0

draw_papers = 0
draw_rock = 0
draw_scissors = 0

attempts = 1

print("\n\t===================== LETS PLAY PAPER,ROCK,SCISSORS===================")
trials = int(input("\nEnter number of times to verse the computer:"))
while attempts <= trials:
    try:
        choice = int(input('Enter a number => 1.PAPER, 2.ROCK, 3.SCISSORS:\n'))
    finally:
        TypeError("Enter a Valid Integer")

    options = ['PAPER', 'ROCK', 'SCISSORS']

    computer = random.choices(options)

    if choice == 1 and computer == ['PAPER']:
        print("your choice PAPER & PAPER = DRAW!")
        draw_papers = draw_papers + 1

    elif choice == 1 and computer == ['ROCK']:
        print("your choice PAPER folds the ROCK ## PLAYER WINS ##")
        pl_wins_paper = pl_wins_paper + 1

    elif choice == 1 and computer == ['SCISSORS']:
        print("your choice PAPER is cut by SCISSORS** COMPUTER WINS!**")
        comp_wins_paper = comp_wins_paper + 1
######################################################

    elif choice == 2 and computer == ['PAPER']:
        print("your choice ROCK is folded by PAPER ** COMPUTER WINS!**")
        comp_wins_rock = comp_wins_rock + 1

    elif choice == 2 and computer == ['ROCK']:
        print("your choice ROCK cant hit a ROCK ***DRAW!")
        draw_rock = draw_rock + 1

    elif choice == 2 and computer == ['SCISSORS']:
        print("your choice ROCK hits the SCISSORS ## PLAYER WINS ##")
        pl_wins_rock = pl_wins_rock + 1
    #####################################################3

    elif choice == 3 and computer == ['PAPER']:
         print("your choice SCISSORS cuts the PAPERS ## PLAYER WINS ##")
         pl_wins_scissors = pl_wins_scissors + 1

    elif choice == 3 and computer == ['ROCK']:
        print("your choice SCISSORS is hit by a ROCK** COMPUTER WINS!**")
        comp_wins_scissors = comp_wins_scissors + 1

    elif choice == 3 and computer == ['SCISSORS']:
        print("your choice SCISSORS cant cut SCISSORS **DRAW!")
        draw_scissors = draw_scissors + 1


    else:
        print("Enter a Valid option)")

    attempts = attempts + 1


def total_player_wins():
    win_of_pl = str(pl_wins_paper + pl_wins_rock + pl_wins_scissors)
    return win_of_pl


def total_draws():
    draw_of_both = str(draw_papers + draw_rock + draw_scissors)
    return draw_of_both


def total_computer_wins():
    win_of_comp = str(comp_wins_paper + comp_wins_rock + comp_wins_scissors)
    return win_of_comp


print("\n\n************SUMMARY OF GAME**************")
print("computer wins:"+total_computer_wins())
print("Player wins:"+total_player_wins())
print("Draws:"+total_draws())
print("Total games played:"+str(trials))


sample = open("gamedata.txt", "a") # open file with file name and mode in a string format
sample.write("computer wins:"+total_computer_wins())
sample.write("Player wins:"+total_player_wins())
sample.write("Draws:"+total_draws())
sample.write("\n\nTotal games played:"+str(trials))

sample.close()


if total_player_wins() > total_computer_wins():
    print("\n\t\t++++++++++++++++++++++++++++++++ CONGRATULATIONS YOU HAVE WON ++++++++++++++++++++++++++++++++")

elif total_player_wins() == total_computer_wins():
    print("\n\t\t+++++++++++++++++++++++++++++++MATCH ENDS IN A DRAW +++++++++++++++++++++++++++++++")

else:
    print("\n\t\t+++++++++++++++++++++++++++++++ OOPS! YOU HAVE LOST +++++++++++++++++++++++++++++++")






