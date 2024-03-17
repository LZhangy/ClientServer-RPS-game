# Art from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

def print_rps_art():
    # Print ascii art for rock, paper and scissors
    print("Playing Rock Paper Scissors")
    # Print a rock
    print("    _______")
    print("---'   ____)")
    print("      (_____)")
    print("      (_____)")
    print("      (____)")
    print("---.__(___)")
    # Print a paper
    print("     _______")
    print("---'    ____)____")
    print("           ______)")
    print("          _______)")
    print("         _______)")
    print("---.__________)")
    # Print scissors
    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("       __________)")
    print("      (____)")
    print("---.__(___)")

def get_player_move():
    # Prompt for a move
    move = input("Enter your move (rock, paper, or scissors) >")
    return move

def gameresult(player, server):
    # Compare the player's move to the server's move
    if player == server:
        return "Tie"
    elif player == "rock":
        if server == "scissors":
            return "Player wins"
        else:
            return "Server wins"
    elif player == "paper":
        if server == "rock":
            return "Player wins"
        else:
            return "Server wins"
    elif player == "scissors":
        if server == "paper":
            return "Player wins"
        else:
            return "Server wins"
    else:
        return "Invalid move"