import time
import random
from abc import ABC, abstractclassmethod
from const import MESSAGES


class AbstractPlayer(ABC):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bet = 0
        self.points = 0
        self.balance = 100

    def calculate_points(self):
        self.points = 0
        for card in self.hand:
            self.points += card.points

    def take_card(self, card):
        self.hand.append(card)
        self.calculate_points()

    def show_hand(self):
        print(f'{self.name} cards: ')
        hand = ''
        for card in self.hand:
            print(card)
        print('Full points: ', self.points)

    def clean_hand(self):
        self.hand.clear()
        self.points = 0

    @abstractclassmethod
    def change_bet(self, min_bet, max_bet):
        pass

    @abstractclassmethod
    def ask_card(self):
        pass


class Player(AbstractPlayer):
    def change_bet(self, min_bet, max_bet):
        while True:
            value = int(input(MESSAGES.get('ask_bet')))
            if value <= max_bet and value >= min_bet:
                self.bet = value
                self.balance -= self.bet
                break
            print('Your bet is: ', self.bet)

    def ask_card(self):
        answer = input(MESSAGES.get('ask_card'))
        if answer == 'y':
            return True
        else:
            return False


class Bot(AbstractPlayer):
    def __init__(self, name):
        super().__init__(name)
        self.max_points = random.randint(17, 20)

    def change_bet(self, min_bet, max_bet):
        self.bet = random.randint(min_bet, max_bet)
        self.balance -= self.bet
        print(self.name, ' bet: ', self.bet)

    def ask_card(self):
        if self.points < self.max_points:
            return True
        else:
            return False


class Dealer(AbstractPlayer):
    max_points = 17

    def change_bet(self, min_bet, max_bet):
        pass

    def ask_card(self):
        if self.points < self.max_points:
            return True
        else:
            return False
