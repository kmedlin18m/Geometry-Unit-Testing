import math
def circle(radius):
    if type(radius) != int and type(radius) != float:
            raise TypeError('Not numeric input')
    if radius <= 0:
        raise ValueError('Not positive')
    area = math.pow(radius, 2)
    area = area * math.pi
    return area
def rectangle(length, width):
    if type(length) != int and type(length) != float:
            raise TypeError('Not numeric input')
    if length <= 0:
        raise ValueError('Not positive')
    if type(width) != int and type(width) != float:
            raise TypeError('Not numeric input')
    if width <= 0:
        raise ValueError('Not positive')
    area = length * width
    return area
def square(length):
    if type(length) != int and type(length) != float:
            raise TypeError('Not numeric input')
    if length <= 0:
        raise ValueError('Not positive')
    area = length * length
    return area
def triangle(length, width):
    if type(length) != int and type(length) != float:
            raise TypeError('Not numeric input')
    if length <= 0:
        raise ValueError('Not positive')
    if type(width) != int and type(width) != float:
            raise TypeError('Not numeric input')
    if width <= 0:
        raise ValueError('Not positive')
    area = (length * width)/2
    return area
