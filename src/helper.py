import random

# Card values for the Blackjack game
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
    'Q': 10, 'K': 10, 'A': 11
}

# List of cards
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

def get_value(hand):
    """
    Calculates the total value of the hand, taking aces into account.

    :param hand: List of cards representing the player's or dealer's hand
    :return: The calculated total value of the hand
    """
    total = 0  # Initialize total value of the hand
    ace_count = 0  # Count the number of aces in the hand

    # Loop through each card in the hand
    for card in hand:
        total += card_values[card]  # Add card value to total sum
        if card == 'A':  # If the card is an ace
            ace_count += 1  # Increase ace counter

    # Adjust the total value if the hand exceeds 21 and aces are present
    while total > 21 and ace_count > 0:
        total -= 10  # Reduce total value by 10 (change ace from 11 to 1)
        ace_count -= 1  # Decrease the number of aces counted as 11

    return total  # Return the calculated total value

def draw_card():
    """
    Draws a random card from the deck.

    :return: A card randomly drawn from the deck
    """
    temp_cards = cards[:]  # Create a copy of the deck
    random.shuffle(temp_cards)  # Shuffle the deck randomly
    return temp_cards.pop(0)  # Draw the top card from the shuffled deck
