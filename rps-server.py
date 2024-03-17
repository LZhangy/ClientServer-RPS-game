#!/usr/bin/env python3

import socket
import rps_game


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
SHUTDOWN_COMMAND = "/q"
RPS_COMMAND = "/rps"


# Citation for the following function:
# Date: 3/5/2024
# Adapted from /OR/ Based on:
# https://realpython.com/python-sockets/#echo-client-and-server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Port might “hang” while testing - set socket reuse option b4 bind 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    print(f"Waiting for client...")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}\n")
        print(f"Note: Play ROCK PAPER SCISSORS with '{RPS_COMMAND}'\n")
        
        is_playing = False
        move = ""
    
        while True:
            # RECEIVING MESSAGES ------------------------------
            data = conn.recv(4096) # All messages sent must be limited to 4096 bytes.
            if not data:
                break
            datad = data.decode()
            
            # Hide response for rock paper scissors
            if is_playing == False:
                print(f"{datad!r}")
            # If we're in a rps game, print the result
            else:
                print(rps_game.gameresult(move, datad))

            # If the client sends the shutdown command, close the connection
            if datad == SHUTDOWN_COMMAND:
                print("Shutdown command received, closing connection.")
                break

            # If the client sends the RPS command, play rock paper scissors 2
            if datad == RPS_COMMAND:
                is_playing = True
                rps_game.print_rps_art()
                
                # Prompt for a move
                move = rps_game.get_player_move()
                # Send the server's move 3
                conn.sendall(move.encode())
                # Wait for the client's move 7
                client_move = conn.recv(4096)
                print(rps_game.gameresult(client_move.decode(), move))
                is_playing = False
            
            
            
                
                
            # SENDING MESSAGES ------------------------------
            message = input("Enter input >")
            conn.sendall(message.encode())

            # If sending the shutdown command, close the connection
            if message == SHUTDOWN_COMMAND:
                print("Shutdown command sent, closing connection.")
                break
            

            # If sending the RPS command, play rock paper scissors
            if message == RPS_COMMAND:
                rps_game.print_rps_art()
                is_playing = True
                move = rps_game.get_player_move()
                # Wait for the client's move
                client_move = conn.recv(4096)
                print(rps_game.gameresult(client_move.decode(), move))
                is_playing = False
                