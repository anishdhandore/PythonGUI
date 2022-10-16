# import tkinter as tk
from tkinter import *
from functions import *

# this is the top label
top_label = Label(root, text="Choose Your Move From Below", font=("Arial", 25))
top_label.place(relx=0.5, rely=0.1, anchor=CENTER) # relx and rely decide what fraction of the screen 

# button for Rock
rock_button = Button(root, text="Rock", font=("Arial", 20), command=choosingRock)
rock_button.place(relx=0.2,rely=0.3, anchor=CENTER)
rock_button.config(width=7, height=3)

# button for Paper
paper_button = Button(root, text="Paper", font=("Arial", 20), command=choosingPaper)
paper_button.place(relx=0.5,rely=0.3, anchor=CENTER)
paper_button.config(width=7, height=3)

# button for Scissor
scissor_button = Button(root, text="Scissor", font=("Arial", 20), command=choosingScissor)
scissor_button.place(relx=0.8,rely=0.3, anchor=CENTER)
scissor_button.config(width=7, height=3)

# print the result here 
res = Label(root, text="", textvariable=result, font=("Arial", 28))
res.place(relx=0.5, rely=0.5, anchor=CENTER)

# label for your choice
mySelection = Label(root, text="You:", font=("Arial", 25))
mySelection.place(relx=0.4, rely=0.7, anchor=CENTER) # relx and rely decide what fraction of the screen 

# label with actual choice
myAns = Label(root, text="", textvariable=myAnswer, font=("Arial", 25))
myAns.place(relx=0.55, rely=0.7, anchor=CENTER) # relx and rely decide what fraction of the screen 

# label for computer's random selection
computerSelection = Label(root, text="Computer:", font=("Arial", 25))
computerSelection.place(relx=0.35, rely=0.8, anchor=CENTER) # relx and rely decide what fraction of the screen 

# label for actual computer's selection
computerAns = Label(root, textvariable=computerAnswer, font=("Arial", 25))
computerAns.place(relx=0.55, rely=0.8, anchor=CENTER) # relx and rely decide what fraction of the screen

root.mainloop()