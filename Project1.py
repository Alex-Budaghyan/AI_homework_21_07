# ChatGpt
class SlottedStruct(type):
    def __new__(cls, name, bases, attrs):
        dimensions = attrs.get('_dimensions', 2)
        for i in range(1, dimensions + 1):
            attrs[f'_{i}'] = attrs.get(f'_{i}', 0)
            attrs[f'dimension{i}'] = property(lambda self, dim=i: getattr(self, f'_{dim}'))

        def __init__(self, *args):
            if len(args) != dimensions:
                raise ValueError(f"Expected {dimensions} argument, got {len(args)}")
            for n, arg in enumerate(args, start=1):
                setattr(self, f'_{n}', arg)
        attrs['__init__'] = __init__

        def __eq__(self, other):
            if not isinstance(other, self.__class__):
                return False
            return all(getattr(self, f'_{i_dimension}') == getattr(other, f'_{i_dimension}')
                       for i_dimension in range(1, dimensions + 1))
        attrs['__eq__'] = __eq__

        def __hash__(self):
            return hash(tuple(getattr(self, f'_{i}') for i in range(1, dimensions + 1)))

        attrs['__hash__'] = __hash__

        return super(SlottedStruct, cls).__new__(cls, name, bases, attrs)


class Point2D(metaclass=SlottedStruct):
    _dimensions = 2

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return f'Point2D: {", ".join(str(getattr(self, f"_{i}")) for i in range(1, 3))}'


class Point3D(metaclass=SlottedStruct):
    _dimensions = 3

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return f'Point3D: {", ".join(str(getattr(self, f"_{i}")) for i in range(1, 4))}'


class Point5D(metaclass=SlottedStruct):
    _dimensions = 5

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return f'Point5D: {", ".join(str(getattr(self, f"_{i}")) for i in range(1, 6))}'


try:
    p2d_1 = Point2D(1, 2)
    p2d_2 = Point2D(1, 2)
    p2d_3 = Point2D(3, 4)
    p3d_1 = Point3D(1, 2, 3)
    p3d_2 = Point3D(1, 2, 3)
    p3d_3 = Point3D(5, 6, 8)
    print(f"{p2d_1}, {p2d_2}, {p2d_3}")
    print(f"{p3d_1}, {p3d_2}, {p3d_3}")
    print(f"{p2d_1 == p2d_2}")
    print(f"{p3d_1 != p3d_3}")
    print(f" {hash(p2d_1)}, {hash(p2d_3)}")
    print(f"{hash(p3d_2)}, {hash(p3d_3)}")

except ValueError as ve:
    print(str(ve))

