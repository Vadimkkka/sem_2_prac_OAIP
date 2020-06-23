# ----------------------------------------------------------
# 2. Создать абстрактный класс Figure с методами вычисления площади и периметра,
# а также методом, выводящим информацию о фигуре на экран.
# Создать производные классы: Rectangle (прямоугольник), Circle (круг), Triangle (треугольник)
# со своими методами вычисления площади и периметра.
# Создать массив n фигур и вывести полную информацию о фигурах на экран.
# ----------------------------------------------------------

from abc import ABC
import math


class Figure(ABC):
    def __init__(self, color):
        self.color = color

    def info(self):
        print('Abstract Base Class')

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def info(self):
        print("Rectangle")
        print("Color:", self.color)
        print("Width:", self.width)
        print("Height:", self.height)
        print("Area:", str(self.area()))
        print("Perimeter:", str(self.perimeter()), '\n')

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height)*2


class Circle(Figure):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def info(self):
        print("Circle")
        print("Color:", self.color)
        print("Radius:", self.radius)
        print("Area:", str(self.area()))
        print("Perimeter:", str(self.perimeter()), '\n')

    def area(self):
        return round(math.pi*math.pow(self.radius, 2), 2)

    def perimeter(self):
        return round(2*math.pi*self.radius, 2)


class Triangle(Figure):
    def __init__(self, a, b, c, color):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def info(self):
        print("Triangle")
        print("Color:", self.color)
        print("A:", self.a)
        print("B:", self.b)
        print("C:", self.c)
        print("Area:", str(self.area()))
        print("Perimeter:", str(self.perimeter()), '\n')

    def area(self):
        p = (self.a + self.b + self.c)/2
        return round(math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c)), 2)

    def perimeter(self):
        return self.a + self.b + self.c


rec = Rectangle(2, 4, 'orange')
cir = Circle(2, 'yellow')
trian = Triangle(2, 3, 4, 'green')

rec.info()
cir.info()
trian.info()
