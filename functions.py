import tkinter as tk
import random

root = tk.Tk()  # initialize
root.title("Rock, Paper, & Scissors")  # giving our GUI a title
root.geometry("800x500")  # setting up the size of the screen

# variables that will be used in main.py
outcomes = ["Rock", "Paper", "Scissor"]
myAnswer = tk.StringVar()
computerAnswer = tk.StringVar()
result = tk.StringVar()

# if user clicks on rock
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

# user chooses paper
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

# user chooses scissor 
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
