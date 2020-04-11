from enum import Enum
import secrets

class CardValue(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def toString(self):
        return self.suit.name + ',' + self.value.name

class Deck():
    def __init__(self):
        self.cards = []
        for val in list(CardValue):
            for suit in list(Suit):
                self.cards.append(Card(suit, val))
        self.shuffle()
        

    # Uses Fisher-Yates shuffle
    def shuffle(self):
        def swap(l, p1, p2):
            temp = l[p1]
            l[p1] = l[p2]
            l[p2] = temp
            return l

        for c in range(len(self.cards) - 1, 0, -1):
            swapLoc = secrets.randbelow(c + 1)
            self.cards = swap(self.cards, swapLoc, c)
