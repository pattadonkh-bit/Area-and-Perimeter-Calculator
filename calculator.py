import math

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def circle_area(radius):
    return math.pi * radius ** 2

def circle_perimeter(radius):
    return 2 * math.pi * radius

def square_area(side):
    return side ** 2

def square_perimeter(side):
    return 4 * side

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c

def parallelogram_area(base, height):
    return base * height

def parallelogram_perimeter(a, b):
    return 2 * (a + b)