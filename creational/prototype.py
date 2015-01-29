__doc__ = """Prototype

Used when the type of objects to create is determined by
a prototypical instance, which is cloned to produce new objects
"""
from abc import ABCMeta, abstractmethod

# We can use either copy.copy() or copy.deepcopy() depend on our needs
from copy import deepcopy as copy


class IPrototype(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def clone(self):
        """
        Clones the instance
        :return: self
        """


class Book(IPrototype):
    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price

    def render_data(self):
        return "<{0}> \"{1}\", {2:.3g}$".format(
            self.author, self.name, self.price
        )

    def clone(self):
        return copy(self)


# Tests
if __name__ == '__main__':
    book = Book("Lewis Carroll", "Alice in Wonderland", 100)
    cloned_book = book.clone()

    assert book.author == cloned_book.author
    assert book.name == cloned_book.name
    assert book.price == cloned_book.price
    assert book.render_data() == cloned_book.render_data()

    assert not id(book) == id(cloned_book)
