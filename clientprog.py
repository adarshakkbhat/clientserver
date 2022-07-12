# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 18:13:43 2022

@author: Adarsha K K
"""

import socket
def client_program():
    host=socket.gethostname()
    port=5000
    client_socket=socket.socket()
    client_socket.connect((host,port))
    message=input("-->")
    while message.lower()!="bye":
        client_socket.send(message.encode())
        data=client_socket.recv(1024).decode()
        print("Received from server :"+data)
        message=input("-->")
    client_socket.close()
client_program()