import random

# Kartenwerte für das Blackjack-Spiel
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
    'Q': 10, 'K': 10, 'A': 11
}

# Kartenliste
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

def get_value(hand):
    """
    Berechnet den Gesamtwert der Hand unter Berücksichtigung der Asse.

    :param hand: Liste von Karten, die die Hand des Spielers oder Dealers repräsentiert
    :return: Der berechnete Gesamtwert der Hand
    """
    total = 0  # Gesamtwert der Hand initialisieren
    ace_count = 0  # Anzahl der Asse in der Hand zählen

    # Schleife über jede Karte in der Hand
    for card in hand:
        total += card_values[card]  # Kartenwert zur Gesamtsumme hinzufügen
        if card == 'A':  # Wenn die Karte ein Ass ist
            ace_count += 1  # Erhöhe den Ass-Zähler

    # Anpassen des Gesamtwerts, wenn die Hand über 21 liegt und Asse vorhanden sind
    while total > 21 and ace_count > 0:
        total -= 10  # Reduziere den Gesamtwert um 10 (Ass von 11 auf 1 ändern)
        ace_count -= 1  # Verringere die Anzahl der Asse, die als 11 gezählt werden

    return total  # Rückgabe des berechneten Gesamtwerts

def draw_card():
    """
    Zieht eine zufällige Karte aus dem Kartendeck.

    :return: Eine Karte, die zufällig aus dem Deck gezogen wird
    """
    temp_cards = cards[:]  # Erstelle eine Kopie des Kartendecks
    random.shuffle(temp_cards)  # Mische das Deck zufällig
    return temp_cards.pop(0)  # Ziehe die oberste Karte aus dem gemischten Deck
