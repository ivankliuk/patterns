__doc__ = """Singleton

Restricts the instantiation of a class to one object
"""


class Singleton(type):
    def __call__(cls, *more):
        if 'instance' not in cls.__dict__:
            cls.instance = super(Singleton, cls).__call__(*more)
        return cls.instance


class Class(object):
    __metaclass__ = Singleton


# Tests
if __name__ == '__main__':
    assert id(Class()) == id(Class())
