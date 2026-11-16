# Program Name: Assignment5.py
	# Course: IT3883/Section 01
	# Student Name: Joel Courtois
	# Assignment Number: Assignment 5
	# Due Date: 11/20/2026
	# Purpose: Creates a database for reading temperatures for Sundays and Thursdays. This takes in ID's as the primary key, and Days of the week and Temperature as Foreign keys. The database reads a text file with the temperatures and then gives back the average of those values for Sundays and Thursdays.

# Import the database
import sqlite3

# Make the database
connection = sqlite3.connect("temperature.db")
cursor = connection.cursor()

# Make the table
cursor.execute(""" CREATE TABLE IF NOT EXISTS Temperature (ID INTEGER PRIMARY KEY, Day_Of_Week TEXT, Temperature_Value REAL) """)

# Read the file then input the numbers
with open ("temperature.txt", "r") as file:
    for line in file:
        day, temperature = line.split()
        cursor.execute("INSERT INTO Temperature (Day_Of_Week, Temperature_Value) VALUES (?,?)", (day.strip(),float(temperature)))
        connection.commit()

# Average for Sundays
cursor.execute(""" SELECT AVG (Temperature_Value) FROM Temperature WHERE Day_Of_Week = 'Sunday' """)

sunday_avg = cursor.fetchone()[0]

cursor.execute(""" SELECT AVG (Temperature_Value) FROM Temperature WHERE Day_Of_Week = 'Thursday' """)

#Average for Thursdays
thursday_avg = cursor.fetchone()[0]

# Print the Averages!
print("Average from Sunday", sunday_avg)
print("Average from Thursday", thursday_avg)

connection.close()