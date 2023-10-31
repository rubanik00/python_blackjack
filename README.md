# Python Blackjack game

## Description

Console game blackjack in Python. Created for educational purposes.

## Installation

1. Clone repository

```bash
git clone https://github.com/rubanik00/python_blackjack.git
```

2. Run

```bash
python3 main.py
```

3. Play

## Blackjack Rules

#### Objective

Blackjack, also known as 21, is a popular card game where the objective is to beat the dealer by having a hand value as close to 21 as possible without exceeding it.

### Setup

- Blackjack is typically played with one or more standard decks of 52 playing cards.
- Numbered cards (2-10) are worth their face value.
- Face cards (Jack, Queen, King) are each worth 10 points.
- Aces - 11 points or 1 point, if the value exceeds 21.

### Gameplay

1. Each player is dealt two cards from the deck, typically face-up, while the dealer receives one face-up and one face-down card.
2. Players take turns deciding whether to "hit" (take another card) or "stand" (keep their current hand).
3. The objective is to get a hand value as close to 21 as possible without exceeding it.
4. If a player's hand exceeds 21 points, they "bust" and lose the game.

### Winning

- If a player's hand equals 21 with their first two cards (an Ace and a 10-value card), they have a "blackjack" and usually win the game.
- If a player's hand is closer to 21 than the dealer's hand without going over, they win the round.
- If the dealer busts and a player hasn't, the player wins.

### Dealer's Rules

- The dealer must hit until their hand is worth 17 points or more.
- If the dealer busts, all remaining players win.

### Ties

- In the case of a tie (push), where a player and the dealer have the same hand value, no money is won or lost.
