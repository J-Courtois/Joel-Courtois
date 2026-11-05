# Program Name: Advanced Application Development
# Course: IT3883/Section 01
# Student Name: Joel Courtois
# Assignment Number: Assignment 4A
# Due Date: 11/06/2026
# Purpose: This program creates a connection between two pycharm coding files through a network connection to one IP address. It takes in a message from the user and makes it all upper case when giving it back to the user.

import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect(("127.0.0.1", 45000))

message = input("What would you like to write?")

tcp_socket.sendall(message.encode())

response = tcp_socket.recv(1024).decode()

print("Here's what you wrote:", response)

tcp_socket.close()