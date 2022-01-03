import os
import random
import tkinter as tk
from tkinter import ttk


def clear():
    os.system("cls" if os.name == "nt" else "clear")


# CONFIG
DIFFICULTYLEVELS_NAME = ("Easy", "Normal", "Hard")  # you can add more
DIFFICULTYLEVELS_MAXNUMBER = (20, 50, 100)  # you can add more
ATTEMPTLEVELS = ("infinite", 3, 5, 10)  # you can add more

# GLOBAL VARIABLES
number = 0
difficultyindex = 0
attempts = 0
remainingattempts = 0
showattempts = True


def configgame():
    configwindow = tk.Tk()
    configwindow.geometry("200x200")
    configwindow.resizable(False, False)

    lbl_difficulty = tk.Label(configwindow, text="Set difficulty:")
    lbl_difficulty.pack()

    selected_difficulty = tk.StringVar()
    selected_difficulty.set(str(DIFFICULTYLEVELS_NAME[0]))
    drop_difficulty = tk.OptionMenu(configwindow, selected_difficulty, *DIFFICULTYLEVELS_NAME)
    drop_difficulty.pack(fill="both")

    configwindow.mainloop()


def setdifficulty():
    global difficultyindex

    clear()
    print("Set the difficulty of the game:")
    for i in range(len(DIFFICULTYLEVELS_NAME)):
        print("[{0}] - {1}".format(i, DIFFICULTYLEVELS_NAME[i]))

    while True:
        d = input()
        if d.isnumeric() and 0 <= int(d) < len(DIFFICULTYLEVELS_MAXNUMBER):
            difficultyindex = int(d)
            break
        print("Invalid input. Try again.")


def setattempts():
    global attempts, remainingattempts, showattempts

    clear()
    print("Set the number of attempts:")
    for i in range(len(ATTEMPTLEVELS)):
        print("[{0}] - {1}".format(i, ATTEMPTLEVELS[i]))

    while True:
        a = input()
        if a.isnumeric() and 0 <= int(a) < len(ATTEMPTLEVELS):
            if int(a) == 0:
                attempts = 9999
                remainingattempts = attempts
                showattempts = False
            else:
                attempts = ATTEMPTLEVELS[int(a)]
                remainingattempts = attempts
                showattempts = True
            break
        print("Invalid input. Enter the number of your choice.")


def generateNumber():
    global number
    number = random.randint(1, DIFFICULTYLEVELS_MAXNUMBER[difficultyindex])

"""
def updatehud():
    lbl_hud.config(text="Difficulty: {0} \nAttempts left: {1}".
                   format(DIFFICULTYLEVELS_NAME[difficultyindex], remainingattempts))


def setcomment(comment: str):
    lbl_comment.config(text=comment)


def on_btn_guess():
    global remainingattempts

    if remainingattempts > -1:
        if txt_guess.get().isnumeric():
            remainingattempts -= 1
            updatehud()
            if int(txt_guess.get()) == number:
                showresultwindow("w")
            elif int(txt_guess.get()) > number:
                if abs(int(txt_guess.get()) - number) <= 3:
                    setcomment("You're very close! Lower!")
                else:
                    setcomment("Lower!")
            elif int(txt_guess.get()) < number:
                if abs(int(txt_guess.get()) - number) <= 3:
                    setcomment("You're very close! Higher!")
                else:
                    setcomment("Higher!")
        else:
            setcomment("Invalid input. Enter a number.")
    else:
        showresultwindow("l")


def showresultwindow(result: str):
    txt_guess.config(state="disabled")
    btn_guess.config(state="disabled")

    resultwindow = tk.Tk()
    resultwindow.resizable(False, False)
    lbl_result = tk.Label(resultwindow, font="Helvetica 12 bold")
    lbl_result.pack()

    if result == "w":
        lbl_result.config(text="You win! The correct number is {0}.\nYou did it in {1} attempts. Congratulations!"
                          .format(number, attempts - remainingattempts))
    else:
        lbl_result.config(text="You ran out of attempts. The correct number is {0}.\nBetter luck next time!"
                          .format(number))
"""

if __name__ == '__main__':
    """
    # creates the GUI
    window = tk.Tk()
    window.title("Number Guessing Game")
    window.geometry("320x240")
    window.resizable(False, False)

    lbl_hud = tk.Label(window)
    lbl_hud.pack(anchor="w")
    # updatehud() - # debug purposes

    ttk.Separator(window, orient="horizontal").pack(fill="x")

    lbl_instruction = tk.Label(window, text="Guess the number from 1 to {0}!"
                               .format(DIFFICULTYLEVELS_MAXNUMBER[difficultyindex]), font="Helvetica 12 bold")
    lbl_instruction.pack()
    lbl_comment = tk.Label()
    lbl_comment.pack()

    txt_guess = tk.Entry(window, font="Helvetica 18 bold", justify="center", width=5)
    txt_guess.pack()

    btn_guess = tk.Button(window, text="Guess", command=on_btn_guess)
    btn_guess.pack()
    """
    # game loop
    configgame()
    # setdifficulty()
    # setattempts()
    # generateNumber()

    # window.mainloop()

