# Program Name: Advanced Application Development
# Course: IT3883/Section 01
# Student Name: Joel Courtois
# Assignment Number: Assignment 1
# Due Date: 09/22/ 2026
# Purpose: This program is a text based menu that asks the user for input and then executes a path depending on what the user gives. It gives the 4 choices of either give preevious inputs, clear old data, display currently saved data, or exit the program.

stored = "(Nothing)"

loop = True
while loop:
    data = ""
    print("The Menu!")
    print("1. Append data")
    print("2. Clear input")
    print("3. Display the input")
    print("4. Exit")
    option = input("What would you like to select?")

    if option == "1":
        data = input("Please enter your data")
        stored = data
        print("Your data is now stored in!")
    elif option == "2":
        stored = "(Nothing)"
        print("Your data is now cleared!")
    elif option == "3":
        print("You have put down, ", stored)
    elif option == "4":
        print("Thanks for your time!")
        loop = False
        break