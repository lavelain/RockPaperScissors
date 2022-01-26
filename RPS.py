# Import Required Library
from tkinter import *
import random

# Create Object
root = Tk()

# Define Window Size
root.geometry("300x300")

# title
root.title("Rock Paper Scissors! Game")

# Computer Values for what to choose
computer_value = {
	"0":"Rock",
	"1":"Paper",
	"2":"Scissor"
}

# Reset The Game
def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text = "Player")
	l3.config(text = "Computer")
	l4.config(text = "")

# Disable buttons after Match is Over
def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"

# If player chooses rock
def isrock():
	c_v = computer_value[str(random.randint(0,2))]
	if c_v == "Rock":
		match_result = "Draw"
	elif c_v=="Scissor":
		match_result = "You Win!"
	else:
		match_result = "Computer Wins"
	l4.config(text = match_result)
	l1.config(text = "Rock")
	l3.config(text = c_v)
	button_disable()

# If player chooses paper
def ispaper():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Paper":
		match_result = "Draw"
	elif c_v=="Scissor":
		match_result = "Computer Wins"
	else:
		match_result = "You Win!"
	l4.config(text = match_result)
	l1.config(text = "Paper")
	l3.config(text = c_v)
	button_disable()

# If player chooses scissors
def isscissor():
	c_v = computer_value[str(random.randint(0,2))]
	if c_v == "Rock":
		match_result = "Computer Wins"
	elif c_v == "Scissor":
		match_result = "Draw"
	else:
		match_result = "You Win!"
	l4.config(text = match_result)
	l1.config(text = "Scissor")
	l3.config(text = c_v)
	button_disable()

# Add Frames
Label(root,
	text = "Rock, Paper, Scissors!",
	font = "normal 20 bold",
	fg = "orange").pack(pady = 25)

frame = Frame(root)
frame.pack()

l1 = Label(frame,
		text = "Player",
		font = 10)

l2 = Label(frame,
		text = "VS",
		font = 10)

l3 = Label(frame,
		text = "Computer",
		font = 10)

l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()

# Define Window 

l4 = Label(root,
		text = "",
		font = "normal 20 bold",
		bg = "white",
		width = 15 ,
		borderwidth = 2,
		relief = "solid")
l4.pack(pady = 25)

frame1 = Frame(root)
frame1.pack()

# Add Buttons

b1 = Button(frame1, text = "Rock",
			font = 10, width = 7,
			command = isrock)

b2 = Button(frame1, text = "Paper ",
			font = 10, width = 7,
			command = ispaper)

b3 = Button(frame1, text = "Scissor",
			font = 10, width = 7,
			command = isscissor)

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)
b3.pack(padx = 10)

Button(root, text = "Reset",
	font = 10, fg = "black",
	bg = "cyan", command = reset_game).pack(pady = 20)

# Run Tkinter
root.mainloop()
