from rectangle import Rectangle, Square, Сircle



# Далее составим два прямоугольника
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# вывод площади наших прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)


print(square_1.get_area_square(),
      square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2]

for figure in figures:
      if isinstance(figure, Square):
            print(figure.get_area_square())
      else:
            print(figure.get_area())

circle_1 = Сircle(5)
circle_2 = Сircle(7)
# выводим площади двух кругов на экран
print(circle_1.get_area_circle(),
      circle_2.get_area_circle())
# выводим площади всех фигур
figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure,Square):
       print(figure.get_area_square())
    elif isinstance(figure,Сircle):
        print(figure.get_area_circle())
    else:
       print(figure.get_area())