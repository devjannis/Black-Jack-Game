# Black Jack Game

This project is a basic implementation of the classic Black Jack card game. The game involves three main components: the dealer, the player, and the game controller. The objective is to achieve a hand value as close to 21 as possible without going over.

## Requirements

- Python 3.x

## Usage

To start the game, run the following command:

```bash
python main.py
```

## Game Components

### Dealer
- The dealer draws cards until reaching a minimum hand value of 17.
- If the dealer's hand exceeds 21, the player automatically wins.

### Player
- The player is dealt two initial cards.
- The player can choose to draw more cards, stand, double down, or surrender.

## Player Actions

1. **Draw**: Draw another card to improve your hand.
2. **Stand**: End your turn and keep your current hand.
3. **Double Down**: Double your stake, draw one additional card, and end your turn.
4. **Surrender**: Forfeit your hand and lose half your stake.

## Features
- Option to place and adjust your bet amount.
