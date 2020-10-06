"""This file defines the classes used by the card game logic in main.py"""

from typing import List
from typing import Union


class Card():
    """ Class defining one card by two arguments:
    :symbol: one of ['♥', '♦', '♣', '♠']
    :number: one of ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    """
    
    color_scheme = {'♥': 'red', '♦': 'red', '♣': 'black', '♠': 'black'}
    
    def __init__(self, symbol: str, number: Union(int, str)):
        self.symbol = symbol
        self.number = number
        self.color = Card.color_scheme[symbol]
    
    def __str__(self):
        string = f"{self.symbol}{self.number}\n"
        return string


class Board():
    """ Class defining a board particular to a card game:
    it contains an active_cards list containing the 6 most
    recent cards played, and an played_cards list
    containing the other already played cards.
    :players: the list of player names
    """
    
    def __init__(self, player_names: List[str]):
        self.players = player_names
        self.active_cards = []
        self.played_cards = []
    
    def __str__(self):
        string = "Active cards:\n"
        for board_player in self.players:
            string += f'{board_player}:'
            for player, card in self.active_cards:
                if board_player == player:
                    string += str(card)
            else:
                string = "\n"
        print("Played cards:\n")
        for board_player in self.players:
            print(f'{board_player}:')
            for player, card in self.played_cards:
                if board_player == player:
                    print(card)
            else:
                print("\n")
        return string
    
    def play_card(self, name: str, card):
        """Receive the card from a player and register
        it as a tuple into the FIFO active_cards list,
        overflowing the 7th card onto played_cards"""
        self.active_cards.append((name, card))
        if len(self.active_cards) == 7:
            self.played_cards.append(self.active_cards[0])
            self.active_cards = self.active_cards[1:]


class Player():
    """ Class defining a player providing a name, a board
    to play on, and a deck of cards from which the top 10 are
    taken
    :name:
    :deck: 
    """
    
    def __init__(self, name: str, deck, board):
        self.name = name
        self.board = board
        self.cards = []
        for i in range(9):
            self.cards.append(deck.pop())
    
    def play(self):
        """plays the top card or returns 'empty'"""
        if len(self.cards) > 0:
            self.board.play_card(name=self.name, card=self.cards.pop())
            print(f'{self.name} played their card.\n')
        else:
            return "empty"
    
    def shuffle():
        random.shuffle(self.cards)
        print(f'{self.name} shuffled their cards.\n')

    
    