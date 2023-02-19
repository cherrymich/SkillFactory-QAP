import pytest

from app.calc import Calculator

class TestingCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self): # проверка сложения
        assert self.calc.adding(self, 5, 7) == 12

    def test_subtraction_success(self): # проверка вычитания
        assert self.calc.subtraction(self, 8, 4) == 4

    def test_multiplication_success(self): # проверка умножения
        assert self.calc.multiplication(self, 2, 3) == 6

    def test_division_success(self): # проверка деления
        assert self.calc.division(self, 6, 3) == 2

    def test_zero_division(self): # проверка деления на нуль, обрабатывается исключение ZeroDivisionError
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 2, 0)

    def teardown(self):
        print('Завершаем тестирование. Закрываем файл проверки. Выполнение метода TearDown')
