# колода карт
import random



class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        if str(val).isdigit():
            self.price = val
        elif val == 'Туз':
            self.price = 11
        else:
            self.price = 10

    def showcard(self):
        print('\t', self.suit, self.val)

class Koloda:
    cards = []
    suits = ['\u2664', '\u2665', '\u2666', '\u2667']
    nums = ['Туз', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король']
    def __init__(self):
        for s in self.suits:
            for n in self.nums:
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
        self.sum = 0

    def showhand(self):
        for card in self.hand:
            card.showcard()

    def showsum(self):
        print('\t', 'Сумма карт =', self.sum)

    def takecard(self, deck, num=1):
        for i in range(num):
            self.hand.append(deck.minuscard())
            self.sum += self.hand[-1].price

    def fold(self):
        self.hand = []
        self.sum = 0



deck1 = Koloda()
deck1.shuffle()

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


boris.fold()
boris.showhand()

name = input('Начнём игру. Введите ваше имя:\n')
player = Player(name)
comp = Player('Компьютер')
deck = Koloda()

def comp_take_card():
    if comp.sum < 11 or (11 <= comp.sum <= 19 and random.choices([True, False], weights=[20-comp.sum, comp.sum-10], k=1)[0]):
        comp.takecard(deck)
        print('Игрок', comp.name, 'взял карту')
        return True
    else:
        print('Игрок', comp.name, 'отказался от добора')
        return False

def check():
    if (player.sum > 21 and comp.sum > 21) or (player.sum == comp.sum):
        print('Ничья')
        res = 0
    elif (player.sum == 21) or (player.sum < 21 < comp.sum) or (comp.sum < player.sum < 21):
        print('Вы выиграли!')
        res = 1
    else:
        print('Вы проиграли =(')
        res = 2
    print('Карты соперника:')
    comp.showhand()
    comp.showsum()
    return res



while True:
    end_game = False
    deck.shuffle()
    player.takecard(deck, 2)
    comp.takecard(deck, 2)
    print('Ваши карты:')
    player.showhand()
    player.showsum()





    while True:
        ans = int(input('Возьмёте ещё карту?\n1 - да\n2 - нет\n'))
        if ans == 1:
            player.takecard(deck)
            print('Ваши карты:')
            player.showhand()
            player.showsum()
        else:
            break

    break
