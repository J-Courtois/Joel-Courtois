# Program Name: Advanced Application Development
# Course: IT3883/Section 01
# Student Name: Joel Courtois
# Assignment Number: Assignment 4B
# Due Date: 11/06/2026
# Purpose: This program creates a connection between two pycharm coding files through a network connection to one IP address. It takes in a message from the user and makes it all upper case when giving it back to the user.

import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.bind(("127.0.0.1", 45000))

tcp_socket.listen(2)

print("Waiting for the connection... ")

connection, address = tcp_socket.accept()

message = connection.recv(1024).decode()

modified_message = message.upper()

connection.sendall(modified_message.encode())

print("We got the message!", message)
print("Sending the new message...", modified_message)

connection.close()
tcp_socket.close()