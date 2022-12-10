import math

class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, a, b):
        
        if a <= 0 or b <= 0:
            raise NonPositiveDigitException('Сторона прямоугольника не может быть равна 0, задайте другой размер')
        self.a = a
        self.b = b
        
                
    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException('Сторона квадрата не может быть равна 0, задайте другой размер')
        
        
        self.a = a
    def get_area_square(self):
        return self.a **2
    
class Circle:
    def __init__(self, r):
        if r <= 0:
            raise NonPositiveDigitException('Радиус окружности не может быть равна 0, задайте другой размер')
        
        
        self.r = r
    def get_area_circle(self):
        return math.pi*self.r **2