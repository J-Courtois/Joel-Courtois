    # Program Name: Assignment3.py (use the name the program is saved as)
	# Course: IT3883/Section 01
	# Student Name: Joel Courtois
	# Assignment Number: Assignment 3
	# Due Date: 10/10/ 2026
	# Purpose: This program is a conversion tool between Miles per Gallon into Kilometers per Liter. This tool uses a GUI application which gives a seperate text box for the user to input the value and get the right conversion.

import tkinter as tk

def convert(event = None):
    try:
        mpg = float(event.widget.get())
        km_l = mpg * 0.425143707
        final.config(text = f"{km_l} KPL")
    except ValueError:
        final.config(text = "Not good!")

space = tk.Tk()
space.title("MPG to KPL")
space.geometry("200x200")

mpg_label = tk.Label(space, text = "MPG is: ")
mpg_label.grid(row = 0, column = 0)

mpg_input = tk.Entry(space)
mpg_input.grid(row = 0, column = 1)

km_label = tk.Label(space, text = "KPL is: ")
km_label.grid(row = 1, column = 0)

final = tk.Label(space, text = "")
final.grid(row = 1, column = 1)

mpg_input.bind("<KeyRelease>", convert)

space.mainloop()