#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    player_choice = input("Choose rock, paper, or scissors: ")
    computer_choice = random.choice(options)
    print(f"Computer chose {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a draw!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        player_score += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
        player_score += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1
    
    print(f"Score: Player {player_score} - {computer_score} Computer")
    break