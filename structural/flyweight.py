__doc__ = """Flyweight

Object that minimizes memory use by sharing as much data as possible
with other similar objects
"""


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class FlyweightFactory(object):
    """Factory based implementation of Flyweight
    """

    def __init__(self, cls):
        self._cls = cls
        self._cache = dict()

    def get_instance(self, *args, **kwargs):
        return self._cache.setdefault(
            (args, tuple(kwargs.items())), self._cls(*args, **kwargs)
        )


def flyweight(cls):
    """Decorator based implementation of Flyweight
    """
    cache = dict()
    return lambda *args, **kwargs: cache.setdefault(
        (args, tuple(kwargs.items())), cls(*args, **kwargs))


# Tests
if __name__ == '__main__':
    factory = FlyweightFactory(Card)
    assert factory.get_instance('Ace', 'Spades') is factory.get_instance('Ace', 'Spades')
    assert id(factory.get_instance('Ace', 'Spades')) == id(factory.get_instance('Ace', 'Spades'))

    DecoratedCard = flyweight(Card)
    assert DecoratedCard('Ace', 'Spades') is DecoratedCard('Ace', 'Spades')
    assert id(DecoratedCard('Ace', 'Spades')) == id(DecoratedCard('Ace', 'Spades'))
