# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Restangle:
    def __init__(self, length: float, width: float = None) -> None:
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length
    def perimetr(self):
        return (self.length + self.width) * 2
    
    def ploshad(self):
        return self.length * self.width

r1 = Restangle(2)
r2 = Restangle(4, 2)
print(r1.length, r1.width)
print(r2.length, r2.width)
print(r1.perimetr(), r2.perimetr())
print(r1.ploshad(), r2.ploshad())
