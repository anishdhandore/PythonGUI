from tkinter import *
import random

root = Tk() # initialize 
root.title("Rock, Paper, & Scissors") # giving our GUI a title
root.geometry("500x500") # setting up the size of the screen

outcomes = ["Rock", "Paper", "Scissor"]
myAnswer = StringVar()
computerAnswer = StringVar()
result = StringVar()

def choosingRock():
    computer = random.choice(outcomes)
    myAnswer.set("Rock")
    computerAnswer.set(computer)

    # TIE conditon
    if (computer == "Rock"):
        result.set("IT IS A TIE!!!")
    # player wins
    elif (computer == "Scissor"): 
        result.set("YOU WIN!!!")
    # computer wins
    elif (computer == "Paper"):
        result.set("YOU LOSE!!!")
    else:
        return None

def choosingPaper():
    computer = random.choice(outcomes)
    myAnswer.set("Paper")
    computerAnswer.set(computer)

    # TIE conditon
    if (computer == "Paper"):
        result.set("IT IS A TIE!!!")
    # player wins
    elif (computer == "Rock"): 
        result.set("YOU WIN!!!")
    # computer wins
    elif (computer == "Scissor"):
        result.set("YOU LOSE!!!")
    else:
        return None

def choosingScissor():
    computer = random.choice(outcomes)
    myAnswer.set("Scissor")
    computerAnswer.set(computer)

    # TIE conditon
    if (computer == "Scissor"):
        result.set("IT IS A TIE!!!")
    # player wins
    elif (computer == "Paper"): 
        result.set("YOU WIN!!!")
    # computer wins
    elif (computer == "Rock"):
        result.set("YOU LOSE!!!")
    else:
        return None