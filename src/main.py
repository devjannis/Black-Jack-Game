from helper import *


class Dealer:
    # Class for the dealer in the Blackjack game

    def __init__(self):
        self.value = 0  # Total value of the dealer's hand
        self.hand = []  # List of cards the dealer holds
        self.draw_until_17()  # Dealer draws cards until the value is at least 17

    def draw_until_17(self):
        # Method to draw cards until the value is at least 17
        while self.value < 17:
            card = draw_card()  # Draw a card
            self.hand.append(card)  # Add the card to the hand
            self.value = get_value(self.hand)  # Calculate the new value of the hand
            if self.value > 21:  # If the value is over 21, the dealer loses
                break

    def __repr__(self):
        # Returns a readable representation of the dealer's hand
        hand = ", ".join(self.hand)
        message = f"Dealer's cards: {hand}; Total value: {self.value}"
        return message


class Player:
    # Class for the player in the Blackjack game

    def __init__(self, bet):
        self.value = 0  # Total value of the player's hand
        self.bet = bet  # Player's bet
        self.hand = []  # List of cards the player holds
        self.get_first_cards()  # Draw the first two cards
        self.draw_cards()  # Allow the player to draw more cards

    def __repr__(self):
        # Returns a readable representation of the player's hand
        cards = ", ".join(self.hand)
        return f"Player's cards: {cards}, Total value: {self.value} and current bet: {self.bet}"

    def get_first_cards(self):
        # Method to draw the first two cards for the player
        try:
            first_card = draw_card()
            second_card = draw_card()
            self.hand.append(first_card)
            self.hand.append(second_card)
            self.value = get_value(self.hand)  # Calculate the value of the hand
        except Exception as e:
            print(f"Error drawing initial cards: {e}")
            self.value = 0

    def get_player_choice(self):
        # Method to choose the player's next move
        while True:
            deck = ", ".join(self.hand)
            print(f"Current hand: {deck}")
            print(f"Current value: {self.value}")
            print("""
1. Draw
2. Stand
3. Double
4. Surrender
            """)
            choice = input("Your choice: ").strip()
            if choice in {"1", "2", "3", "4"}:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def draw_cards(self):
        # Method to draw cards based on the player's choice
        while True:
            choice = self.get_player_choice()  # Get the player's choice
            if choice == "1":  # Draw a new card
                try:
                    card = draw_card()
                    self.hand.append(card)
                except Exception as e:
                    print(f"Error drawing a card: {e}")
                    continue
            elif choice == "2":  # Stand, do not draw any more cards
                break
            elif choice == "3":  # Double: Double the bet and draw a new card
                if self.bet > 0:
                    self.bet *= 2
                    try:
                        card = draw_card()
                        self.hand.append(card)
                    except Exception as e:
                        print(f"Error drawing a card: {e}")
                        continue
                else:
                    print("Not enough bet to double.")
                    continue
            elif choice == "4":  # Surrender: Halve the bet
                self.bet /= 2
                print("You have surrendered.")
                break

            self.value = get_value(self.hand)  # Calculate the new value of the hand
            if self.value > 21:  # If the value is over 21, the player loses
                break


class Game:
    # Class for the entire Blackjack game

    def __init__(self):
        self.player = None
        self.player_bet = 0
        self.dealer = None

    def __call__(self, *args, **kwargs):
        self.dealer = Dealer()  # Create a Dealer instance and draw its cards
        self.get_bets()  # Ask the player for their bet
        self.show_hands(reveal_dealer=False)  # Show the dealer's hand without revealing all cards
        self.player = Player(self.player_bet)  # Create a Player instance and draw their cards
        self.end_game()  # End the game and show the result

    def get_bets(self):
        # Method to get the player's bet
        while True:
            try:
                bet = input("How much would you like to bet? ").strip()
                if bet.isdigit():
                    if int(bet) > 0:
                        self.player_bet = int(bet)
                        break
                    else:
                        print("The bet must be greater than 0.")
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Invalid value. Please enter a valid number.")

    def show_hands(self, reveal_dealer=False, reveal_player=False):
        # Method to show the hands of the dealer and player
        if reveal_player:
            print(self.player)
        if reveal_dealer:
            print(self.dealer)
        else:
            print(f"Dealer's hand: {self.dealer.hand[0]}, [hidden]")

    def end_game(self):
        # Method to show the result of the game
        self.show_hands(reveal_dealer=True, reveal_player=True)

        if self.player.value > 21 and self.dealer.value > 21:
            print("Both have busted! No winner.")
        elif self.dealer.value > 21:
            print("Player wins! Dealer has busted.")
        elif self.player.value > 21:
            print("Dealer wins! Player has busted.")
        elif self.dealer.value == 21 and self.player.value == 21:
            print("Draw! Both have Blackjack.")
        elif self.player.value == 21:
            print("Player wins with Blackjack!")
        elif self.dealer.value == 21:
            print("Dealer wins with Blackjack!")
        elif 21 >= self.player.value == self.dealer.value and self.dealer.value <= 21:
            print("Draw!")
        elif 21 >= self.player.value > self.dealer.value:
            print("Player wins! Dealer loses.")
        elif 21 >= self.dealer.value > self.player.value:
            print("Dealer wins!")
        else:
            print("Error: Invalid game state!")


game = Game()
game()
