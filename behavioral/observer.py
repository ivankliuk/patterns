__doc__ = """Observer

Used to allow an object to publish changes to its state.
Other objects subscribe to be immediately notified of any changes.

Also nice implementation:
http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Observer
"""
from abc import ABCMeta, abstractmethod


class AbstractSubject(object):
    __metaclass__ = ABCMeta

    _observers = set()

    def attach(self, observer):
        """Attach observer to the subject

        :param observer:
        :return: None
        """
        self._observers.add(observer)

    def detach(self, observer):
        """Detach observer from the subject

        :param observer:
        :return: None
        """
        self._observers.remove(observer)

    def notify(self, modifier=None):
        """Notify observers

        :param modifier:
        :return: None
        """
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class AbstractObserver(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, subject):
        """Update observer

        :param subject: Subject()
        :return: None
        """
        pass


class WeatherBoard(AbstractSubject):
    @property
    def observers(self):
        """List all observers connected to the subject.
        Added for convenience.

        :return: set() of observers
        """
        return self._observers

    def set_new_temp(self, new_temp):
        self.temp = new_temp
        self.notify()


class Client(AbstractObserver):
    def __init__(self):
        self.temp = 0

    def update(self, subject):
        self.temp = subject.temp


# Tests
if __name__ == '__main__':
    subj = WeatherBoard()
    obs1 = Client()
    obs2 = Client()
    obs3 = Client()

    subj.attach(obs1)
    subj.attach(obs2)
    subj.attach(obs3)

    subj.set_new_temp(10)
    assert obs1.temp == 10
    assert obs2.temp == 10
    assert obs3.temp == 10

    subj.detach(obs3)
    subj.set_new_temp(20)
    assert obs1.temp == 20
    assert obs2.temp == 20
    assert obs3.temp == 10

    subj.attach(obs3)
    subj.set_new_temp(30)
    assert obs1.temp == 30
    assert obs2.temp == 30
    assert obs3.temp == 30
