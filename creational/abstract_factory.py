__doc__ = """Abstract factory

Provide an interface for creating families of related or dependent objects
without specifying their concrete classes.
"""
from abc import ABCMeta, abstractmethod
import unittest

_suits = ("spades", "hearts", "diamonds", "clubs")
_36_deck = ("6", "7", "8", "9", "10", "Ace", "King", "Queen", "Jack")
_52_deck = ("2", "3", "4", "5") + _36_deck


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class AbstractCardFactory(object):
    """Abstract factory class
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_deck(self):
        """Return all cards in the deck"""
        pass

    @abstractmethod
    def get_suit(self, suit):
        """Return all cards in the suit"""
        pass


class ConcreteFactoryDeck36(AbstractCardFactory):
    def get_deck(self):
        deck = list()
        for suit in _suits:
            for value in _36_deck:
                deck.append(Card(value, suit))
        return deck

    def get_suit(self, suit):
        if suit in _suits:
            return [Card(value, suit) for value in _36_deck]
        raise ValueError("No such suit!")


class ConcreteFactoryDeck52(AbstractCardFactory):
    def get_deck(self):
        deck = list()
        for suit in _suits:
            for value in _52_deck:
                deck.append(Card(value, suit))
        return deck

    def get_suit(self, suit):
        if suit in _suits:
            return [Card(value, suit) for value in _52_deck]
        raise ValueError("No such suit!")


# Tests
class AbstractFactoryTests(unittest.TestCase):
    def setUp(self):
        self.factory36 = ConcreteFactoryDeck36()
        self.factory52 = ConcreteFactoryDeck52()
        self.tuples_deck36 = [(card.value, card.suit) for card in
                              self.factory36.get_deck()]
        self.tuples_deck52 = [(card.value, card.suit) for card in
                              self.factory52.get_deck()]
        self.tuples_suit36 = [(card.value, card.suit) for card in
                              self.factory36.get_deck()]
        self.tuples_suit52 = [(card.value, card.suit) for card in
                              self.factory52.get_deck()]

    def test_length(self):
        self.assertEqual(len(self.factory36.get_deck()), 36)
        self.assertEqual(len(self.factory52.get_deck()), 52)

    def test_factory_returns_list(self):
        self.assertIsInstance(self.factory36.get_deck(), list)
        self.assertIsInstance(self.factory52.get_deck(), list)

    def test_factory_returns_cards_in_list(self):
        for card in self.factory36.get_deck():
            self.assertIsInstance(card, Card)

        for card in self.factory52.get_deck():
            self.assertIsInstance(card, Card)

    def test_deck(self):
        for suit in _suits:
            for value in _36_deck:
                self.assertIn((value, suit), self.tuples_deck36)

            for value in _52_deck:
                self.assertIn((value, suit), self.tuples_deck52)

    def test_suit(self):
        for value in _36_deck:
            self.assertIn((value, "diamonds"), self.tuples_suit36)

        for value in _52_deck:
            self.assertIn((value, "spades"), self.tuples_suit52)

    def test_wrong_suit(self):
        self.assertRaises(ValueError, self.factory36.get_suit, "shamrocks")
        self.assertRaises(ValueError, self.factory52.get_suit, "shamrocks")


# Tests
if __name__ == '__main__':
    unittest.main()
