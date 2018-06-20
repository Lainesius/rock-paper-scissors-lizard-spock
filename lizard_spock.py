import random

SCORE_GOAL = 3

POOL = ["stone", "scissors", "paper", "lizard", "spock"]

WIN_CONDITIONS = {
    "stone": {"scissors", "lizard"},
    "scissors": {"paper", "lizard"},
    "paper": {"stone", "spock"},
    "lizard": {"paper", "spock"},
    "spock": {"stone", "scissors"}
}

def game():
    """Main function that keeps the game running until one side wins.

    Takes no arguments.

    Returns:
        True if player won the game, False otherwise
    """
    player_score = ai_score = 0
    while player_score < SCORE_GOAL and ai_score < SCORE_GOAL:
        # returns true if player won
        if play_round():
            player_score += 1
        else:
            ai_score += 1
        print("Current score: You {}-{} Opponent".format(player_score, ai_score))
    if player_score == SCORE_GOAL:
        print("Congratulations, you won!")
        return True
    else:
        print("You lost.")
        return False

def play_round():
    """Goes through a single round by the set rules. In case of a tie, the round
    is replayed until a winner is found.

    Takes no arguments.

    Returns:
        True if player won the round, False otherwise
    """
    while True:
        player_choice = get_valid_input()
        ai_choice = random.choice(POOL)
        if player_choice == ai_choice:
            print("Opponent chose {} as well, it's a tie!".format(ai_choice))
            continue
        if ai_choice in WIN_CONDITIONS[player_choice]:
            print("Opponent chose {}, you win this round!".format(ai_choice))
            return True
        else:
            print("Opponent chose {}, you lost this round...".format(ai_choice))
            return False

def get_valid_input():
    """Gets a valid case-insensitive choice for the game from a player.

    Takes no arguments.

    Returns:
        String that is guaranteed to be in the POOL
    """
    while True:
        print("Make your choice: stone, scissors, paper, lizard or spock!")
        player_choice = input()
        if not isinstance(player_choice, str):
            print("Invalid input, try again!")
            continue
        player_choice = player_choice.lower()
        if player_choice not in POOL:
            print("Invalid input, try again!")
            continue
        return player_choice

game()
