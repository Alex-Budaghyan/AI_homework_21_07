class SingletonMeta(type):
    _instances = {}

    def __new__(cls, name, bases, attr):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__new__(cls, name, bases, attr)
        return cls._instances[cls]

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Bool(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"This is {self.__class__.__name__} class which metaclass is SingletonMeta"


class Hundred(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"This is {self.__class__.__name__} class which metaclass is SingletonMeta"


b1 = Bool([])
b2 = Bool(True)
print(b2.__str__())
a1 = Hundred(741)
a2 = Hundred(456)
print(a1.__repr__())
print(b1 is b2)
print(a1 is a2)
# print(b1 in a1)