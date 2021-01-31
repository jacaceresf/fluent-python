import collections
import random
# from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
# print(f'Getting the first card {deck[0]}')
# print(f'Getting the last card {deck[-1]}')

print(random.choice(deck))

#looking at the top three cards from a deck
print(deck[:3])

for card in deck:
    print(card)

#iterate the deck in reverse
for card in reversed(deck):
    print(card)