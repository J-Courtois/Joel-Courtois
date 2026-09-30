	# Program Name: Assignment2.py
	# Course: IT3883/Section 01
	# Student Name: Joel Courtois
	# Assignment Number: Assignment 2
	# Due Date: 09/30/ 2026
	# Purpose: This program uses a coding file and a text file to calcualte the grades of three students; Bob, Jack and Jane. The 6 grades are put into a text file, read by the code and divided with an array list. Then if statements are used for each case to put the students average grade into descending order.

 # Open the text file
file = open("grades.txt", "r")

# Have the text file be read when values are put in via an array list
bob = file.readline().split()
jack = file.readline().split()
jane = file.readline().split()

# Close the text file
file.close()

# Collect the values as a float to divide them by six and get a decimal number
bobs_avg = (float(bob[1]) + float(bob[2]) + float(bob[3]) + float(bob[4]) + float(bob[5]) + float(bob[6])) / 6
jacks_avg = (float(jack[1]) + float(jack[2]) + float(jack[3]) + float(jack[4]) + float(jack[5]) + float(jack[6])) / 6
jane_avg = (float(jane[1]) + float(jane[2]) + float(jane[3]) + float(jane[4]) + float(jane[5]) + float(jane[6])) / 6

# Each if statement for every case for descending order
# f print is used to print the average and not the variable name
if bobs_avg > jacks_avg > jane_avg:
    print (f"Bob {bobs_avg} \n Jack {jacks_avg} \n Jane {jane_avg}")

elif bobs_avg > jane_avg > jacks_avg:
    print (f"Bob {bobs_avg} \n Jane {jane_avg} \n Jack {jacks_avg}")

elif jane_avg > bobs_avg > jacks_avg:
    print (f"Jane {jane_avg} \n Bob {bobs_avg} \n Jack {jacks_avg}")

elif jane_avg > jacks_avg > bobs_avg:
    print (f"Jane {jane_avg} \n Jack {jacks_avg} \n Bob {bobs_avg}")

elif jacks_avg > bobs_avg > jane_avg:
    print (f"Jack {jacks_avg} \n Bob {bobs_avg} \n Jane {jane_avg}")

elif jacks_avg > jane_avg > bobs_avg:
    print (f"Jack {jacks_avg} \n Jane {jane_avg} \n Bob {bobs_avg}")