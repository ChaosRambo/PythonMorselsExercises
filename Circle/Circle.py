import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2.0

    @area.setter
    def area(self, area):
        raise AttributeError('can\'t set attribute')

    def __repr__(self):
        return f"Circle({self.radius})"
