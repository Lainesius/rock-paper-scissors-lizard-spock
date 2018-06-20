import random

score_goal = 3

pool = ["stone", "scissors", "paper", "lizard", "spock"]

win_conditions = {
    "stone": {"scissors", "lizard"},
    "scissors": {"paper", "lizard"},
    "paper": {"stone", "spock"},
    "lizard": {"paper", "spock"},
    "spock": {"stone", "scissors"}
}

def game():
    player_score = ai_score = 0
    while player_score < score_goal and ai_score < score_goal:
        # returns true if player won
        if play_round():
            player_score += 1
        else:
            ai_score += 1
        print("Current score: You {}-{} Opponent".format(player_score, ai_score))
    if player_score == score_goal:
        print("Congratulations, you won!")
    else:
        print("You lost.")

def play_round():
    while True:
        player_choice = get_valid_input()
        ai_choice = random.choice(pool)
        if player_choice == ai_choice:
            print("Opponent chose {} as well, it's a tie!".format(ai_choice))
            continue
        if ai_choice in win_conditions[player_choice]:
            print("Opponent chose {}, you win this round!".format(ai_choice))
            return True
        else:
            print("Opponent chose {}, you lost this round...".format(ai_choice))
            return False

def get_valid_input():
    while True:
        print("Make your choice: stone, scissors, paper, lizard or spock!")
        player_choice = input()
        if not isinstance(player_choice, str):
            print("Invalid input, try again!")
            continue
        player_choice = player_choice.lower()
        if player_choice not in pool:
            print("Invalid input, try again!")
            continue
        return player_choice

game()