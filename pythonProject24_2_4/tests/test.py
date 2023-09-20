import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self): # позитивный тест на сложение
        assert  self.calc.adding(self, 1, 1) == 2

    def test_adding_unsuccess(self): # негативный тест на сложение
        assert self.calc.adding(self, 1, 1) == 3


    def test_subtraction_success(self):  # позитивный тест на вычитание
        assert self.calc.subtraction(self, 9, 7) == 2



    def test_zero_division(self):  # тест деление на нуль, обрабатывается исключение ZeroDivisionError
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)



    def test_multiply_success(self):  # позитивный тест на умножение
        assert self.calc.multiply(self, 2, 5) == 10


    def test_multiply_unsuccess(self):   # негативный тест на умножение
         assert self.calc.multiply(self, 3, 5) == 14

    def test_divsion_success(self):  # позитивный тест на деление
        assert self.calc.division(self, 8, 4) == 2


    def teardown(self):
        print("Завершаем тестирование. Закрываем файл проверки. Выполнение метода Teardown")

