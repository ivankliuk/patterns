__doc__ = """Strategy (Policy)

Enables an algorithm's behavior to be selected at runtime
"""
from abc import ABCMeta, abstractmethod
from random import shuffle


class AbstractListHandlerStrategy(object):
    """Strategy interface for list basic operations
    """

    __metaclass__ = ABCMeta

    def __init__(self, lst):
        self._list = lst

    @abstractmethod
    def sort(self):
        """
        Sorts a given list

        :return: list()
        """
        pass

    @abstractmethod
    def reverse_sort(self):
        """
        Reversed sort of a given list

        :return: list()
        """
        pass

    def evens(self):
        """
        Returns list of even index elements

        :return: list()
        """
        return self._list[::2]

    def odds(self):
        """
        Returns list of odd index elements

        :return: list()
        """
        return self._list[1::2]


class ShortListStrategy(AbstractListHandlerStrategy):
    def _insertion_sort(self, reverse=False):
        """Implementation of insertion sort algorithm.
        Should be faster for short lists.
        """
        # This fancy code generates lambda for straight or reversed sort
        if not reverse:
            le_ge = lambda x, y: x > y
        else:
            le_ge = lambda x, y: x < y

        # We work only with the copy of original list
        a = self._list[:]

        # We start from the 2nd index: 1, 2, 3, ..., n
        for i in xrange(1, len(a)):
            curr = a[i]
            prev_key = i - 1
            while prev_key >= 0 and le_ge(a[prev_key], curr):
                a[prev_key + 1] = a[prev_key]
                a[prev_key] = curr
                prev_key -= 1

        return a

    def sort(self):
        return self._insertion_sort()

    def reverse_sort(self):
        return self._insertion_sort(reverse=True)


class LongListStrategy(AbstractListHandlerStrategy):
    def sort(self):
        return sorted(self._list)

    def reverse_sort(self):
        return sorted(self._list, reverse=True)


class Context(object):
    def __init__(self, lst, strategy):
        self._strategy = strategy(lst)

    def __getattr__(self, attr):
        if attr in dir(self._strategy):
            return getattr(self._strategy, attr)
        error_msg = ("'{0}' object has no attribute"
                     " '{1}'".format(self.__class__.__name__, attr))
        raise AttributeError(error_msg)


# Tests
if __name__ == '__main__':
    short_list = range(1, 21)
    long_list = range(1, 1001)
    shuffle(short_list)
    shuffle(long_list)

    client_short = Context(short_list, ShortListStrategy)
    client_long = Context(long_list, LongListStrategy)

    assert client_short.sort() == range(1, 21)
    assert client_long.sort() == range(1, 1001)

    assert client_short.reverse_sort() == range(1, 21)[::-1]
    assert client_long.reverse_sort() == range(1, 1001)[::-1]

    assert client_short.evens() == short_list[::2]
    assert client_long.evens() == long_list[::2]

    assert client_short.odds() == short_list[1::2]
    assert client_long.odds() == long_list[1::2]
