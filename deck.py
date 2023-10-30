from itertools import product
from random import shuffle
from const import RANKS, SUITS, PRINTED


class Card:
    def __init__(self, suit, points, picture):
        self.suit = suit
        self.points = points
        self.picture = picture

    def __str__(self):
        message = self.picture + '\nPoints: ' + str(self.points)
        return message


class Deck:
    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    def _generate_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):
            points = RANKS.get(rank)
            picture = PRINTED.get(rank)
            c = Card(suit=suit, points=points, picture=picture)
            cards.append(c)

        return cards

    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
