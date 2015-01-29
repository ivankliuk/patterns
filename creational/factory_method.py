__doc__ = """Factory method

The factory pattern is used to replace class constructors, abstracting the process of object generation
so that the type of the object instantiated can be determined at run-time.
"""

_suits = ("spades", "hearts", "diamonds", "clubs")
_values = ("Ace", "King", "Queen", "Jack")


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class CardFactory(object):
    def get_4_aces(self):
        """
        Return four aces

        :param suit:
        :return: list() of Card
        """
        return (Card("Ace", suit) for suit in _suits)

    def get_pair(self, card):
        """
        Return a pair for card

        :param card:
        :return: list() of Card
        """
        for s in _suits:
            if card.suit != s:
                suit = s
                break

        value = card.value
        return card, Card(value, suit)


# Tests
if __name__ == '__main__':
    factory = CardFactory()
    assert [(ace.value, ace.suit) for ace in factory.get_4_aces()] == zip(["Ace"] * 4, list(_suits))

    pair = factory.get_pair(Card("Queen", "spades"))
    assert pair[0].value == "Queen"
    assert pair[0].suit == "spades"

    assert pair[1].value == "Queen"
    assert pair[1].suit != "spades"
