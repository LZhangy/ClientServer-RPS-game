#!/usr/bin/env python3

import socket
import rps_game

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
SHUTDOWN_COMMAND = "/q"
RPS_COMMAND = "/rps"



# Citation for the following function:
# Date: 3/5/2024
# Adapted from /OR/ Based on:
# https://realpython.com/python-sockets/#echo-client-and-server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Note: Play ROCK PAPER SCISSORS with '{RPS_COMMAND}'\n")
    
    is_playing = False
    move = ""
    # Loop while connected:
    while True:    
        # SENDING MESSAGES ------------------------------
        message = input("Enter input >")
        s.sendall(message.encode()) # 1
        # If sending the shutdown command, close the connection
        if message == SHUTDOWN_COMMAND:
            print("Shutdown command sent, closing connection.")
            break
        # If sending the RPS command, play rock paper scissors
        if message == RPS_COMMAND:
            is_playing = True
            rps_game.print_rps_art()
            # Wait for the server's move 4
            server_move = s.recv(4096) 
            # Prompt for a move 5
            move = rps_game.get_player_move()
            # Send the client's move 6
            s.sendall(move.encode())
            print(rps_game.gameresult(move, server_move.decode()))
            is_playing = False


        # RECEIVING MESSAGES ------------------------------
        data = s.recv(4096) # All messages sent must be limited to 4096 bytes.        
        datad = data.decode()
        
        # Hide response for rock paper scissors
        if is_playing == False:
            print(f"{datad!r}")
        # If we're in a rps game, print the result
        else:
            rps_game.gameresult(move, datad)
            
        
        if datad == SHUTDOWN_COMMAND:
            print("Shutdown command received, closing connection.")
            break

        # If the server sends the RPS command, start rock paper scissors
        if datad == RPS_COMMAND:
            print("Playing Rock Paper Scissors")
            rps_game.print_rps_art()
            move = rps_game.get_player_move()
            
            # Send the client's move
            conn.sendall(move.encode())
            # Wait for the server's move
            server_move = conn.recv(4096)

            print(rps_game.gameresult(server_move.decode(), move))
