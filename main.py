"""This file holds the logic for running a new game"""

import random

from IPython.display import clear_output

import utils.game

# start the first run of a game
game_active = True
run = 1
while game_active:
    # create a full deck of cards
    card_symbols = ['♥', '♦', '♣', '♠']
    card_numbers = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    mydeck = []
    for symbol in card_symbols:
        for number in card_numbers:
            mydeck.append(utils.game.Card(symbol, number))
    random.shuffle(mydeck)

    # get player details
    if run == 1:
        player_names = ['']
        while len(player_names) > 5 or len(player_names) == 1:
            players_input = input("Please enter the player names separated by commas (max 5):")
            player_names = players_input.split(sep=',')
        else:
            print(f"{len(player_names)} players registered; {','.join(player_names)}")

    # create a board
    myboard = utils.game.Board(player_names)

    # create players with 10 cards each
    players = [utils.game.Player(name=player_name, deck=mydeck, board=myboard) for player_name in player_names]

    # play the game on semi-autopilot
    cards_left_to_play = True
    while cards_left_to_play:
        for player in players:
            if player.play() == "empty":
                cards_left_to_play = False
                break
            else:
                player.play()
        else:
            clear_output(wait=True)
            print(myboard)
    
    # replay (reusing the same players, or stop)
    
    replay_answer = input("Game finished! Type 'y' if you want to go again.")
    if replay_answer == 'y':
        run += 1
    else:
        game_active = False
else:
    print("Card game stopped")



