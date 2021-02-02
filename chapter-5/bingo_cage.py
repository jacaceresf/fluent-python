import random

class BingoCage:

    def __init__(self, items):
        '''Accepts any iterable and build a local copy that prevents unexpected side effects'''
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('you are trying to pick from empty BingoCage')

    def __call__(self):
        return self.pick()

bingo = BingoCage(range(123))

print(bingo.pick())
print(bingo())
