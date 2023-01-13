import random

# ระบบสุ่มโดยฝั่งคอมพิวเตอร์
def get_computer_move():
    moves = ["rock", "paper", "scissors"]
    return random.choice(moves)

# ระบบการแพ้-ชนะ
def get_winner(player_move, computer_move):
    if player_move == computer_move:
        return "Tie"
    elif player_move == "rock" and computer_move == "scissors":
        return "You Win!"
    elif player_move == "paper" and computer_move == "rock":
        return "You Win!"
    elif player_move == "scissors" and computer_move == "paper":
        return "You Win!"
    else:
        return "You Lose!"

# ระบบการเล่นเกม
def play_game():
    player_move = input("Enter your move (rock, paper, scissors): ").lower()
    computer_move = get_computer_move()
    print("Computer move: {}".format(computer_move))
    result = get_winner(player_move, computer_move)
    print(result)

play_game()
