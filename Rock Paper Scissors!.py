def rps(p1, p2):    
    if p1 == "scissors" and p2 == "paper":
        return f"Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return f"Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
        return f"Player 1 won!"
    elif p1 == p2:
        return f"Draw!"
    else:
        return f"Player 2 won!"


"""Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!""""
