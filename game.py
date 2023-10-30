import random
import time

from player import Player, Bot, Dealer
from deck import Deck
from const import MESSAGES, NAMES


class Game:
    max_bots = 4

    def __init__(self):
        self.players = []
        self.player = None
        self.player_position = None
        self.dealer = Dealer("Dealer")
        self.all_players_count = 1
        self.deck = Deck()
        self.min_bet, self.max_bet = 5, 20

    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice in ['y', 'n']:
                return choice == 'y'

    def _launching(self):
        while True:
            bots_count = int(input('Enter bots count (max 4): '))
            if bots_count <= self.max_bots:
                break
        self.all_players_count += bots_count

        for i in range(bots_count):
            self.players.append(Bot(NAMES[i]))
            print(NAMES[i], ' Bot added')

        player_name = input(MESSAGES.get('ask_name'))
        self.player = Player(player_name)
        self.player_position = random.randint(0, self.all_players_count)
        print('Your position is:', self.player_position)
        self.players.insert(self.player_position, self.player)

    def ask_bet(self):
        for player in self.players:
            player.change_bet(self.min_bet, self.max_bet)
            time.sleep(1)

    def ask_card(self):
        for player in self.players:
            while player.ask_card():
                print(f'{player.name} player take card ')
                player.take_card(self.deck.get_card())
                time.sleep(2)

                if isinstance(player, Player):
                    player.show_hand()

                if self.check_overload(player):
                    print(f'{player.name} player has overload')
                    time.sleep(2)
                    self.remove_player(player)
                    break

    def first_deal(self):
        for player in self.players:
            player.take_card(self.deck.get_card())
            player.take_card(self.deck.get_card())

        self.dealer.take_card(self.deck.get_card())
        print('Dealer has first card: ')
        time.sleep(1)
        self.dealer.show_hand()

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)

    def check_overload(self, player):
        if player.points > 21:
            return True
        else:
            return False

    def check_winner(self):
        if self.dealer.points > 21:
            print('Dealer has overload')
            time.sleep(1)

            for player in self.players:
                player.balance += player.bet * 2
                print('All players win')
        else:
            for player in self.players:
                if player.points > self.dealer.points:
                    player.balance += player.bet * 2
                    print(f'{player.name} player win')
                elif player.points == self.dealer.points:
                    player.balance += player.bet
                    print(MESSAGES.get('eq').format(
                        player=player.name, points=player.points))
                else:
                    print(f'{player.name} player lose')

    def play_with_dealer(self):
        while self.dealer.ask_card():
            self.dealer.take_card(self.deck.get_card())
        print('Dealer has: ')
        time.sleep(1)
        self.dealer.show_hand()

    def start_game(self):
        message = MESSAGES.get('ask_start')
        # todo: max players count?
        if not self._ask_starting(message=message):
            exit(1)

        # generating data for starting
        self._launching()

        while True:
            # ask about bet
            self.ask_bet()

            # give first cards to the players
            self.first_deal()

            # print player cards after first deal
            self.player.show_hand()

            # ask players about cards
            self.ask_card()

            self.play_with_dealer()

            self.check_winner()

            if not self._ask_starting(MESSAGES.get('rerun')):
                break

            # todo: change players pos
            # todo: check all players for balance


Game.asd = 10
