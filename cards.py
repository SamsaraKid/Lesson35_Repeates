# колода карт
import random

suits = ['\u2664', '\u2665', '\u2666', '\u2667']
nums = ['Туз', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король']

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def showcard(self):
        print(self.suit, '-', self.val)

class Koloda:
    cards = []
    def __init__(self):
        for s in suits:
            for n in nums:
                self.cards.append(Card(s, n))

    def showdeck(self):
        for c in self.cards:
            c.showcard()

    def shuffle(self):
        random.shuffle(self.cards)

    def minuscard(self):
        return self.cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def showhand(self):
        for card in self.hand:
            card.showcard()

    def takecard(self, deck):
        self.hand.append(deck.minuscard())


deck1 = Koloda()
deck1.shuffle()
# c1 = deck1.minuscard()
# c1.showcard()
print('Игрок Боб')
bob = Player('Bob')
for i in range(3):
    bob.takecard(deck1)
bob.showhand()
print('Игрок Борис')
boris = Player('Boris')
for i in range(3):
    boris.takecard(deck1)
boris.showhand()