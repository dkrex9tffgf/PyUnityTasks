import unittest

from parameterized import parameterized

from PyUnityTasks.BaseUnityTest import BaseUnityTest
from PyUnityTasks.CalculatorObject import CalculatorObject


class CalculatorTest(BaseUnityTest):

    def setUp(self):
        super().setUp()
        self.calc = CalculatorObject(self.unity_driver)

    @parameterized.expand([
        ("both_positive", 3, 2, "5"),
        ("both_negative", -3, -2, "-5")
    ])
    def test_sum(self, name, x, y, result):
        self.calc.sum(x, y)
        self.calc.check_result_equals(result)

    def test_subtracting(self):
        self.calc.subtract(5, 3)
        self.calc.check_result_equals("2")

    @parameterized.expand([
        ("both_positive", 2, 3, "6"),
        ("scientific_notation_result", 10000000000, 10, "1E+11"),
        ("scientific_notation_result_negative", 10000000000, -10, "-1E+11")
    ])
    def test_multiply(self, name, x, y, result):
        self.calc.multiply(x, y)
        self.calc.check_result_equals(result)

    @parameterized.expand([
        ("natural", 12, 3, "4"),
        ("fraction", 1.2, 3.7, "0.3243243"),
        ("scientific_notation_negative_power", 2, 10000000000, "2E-10"),
        ("fraction_round", 2, 3, "0.6666667")
    ])
    def test_division(self, name, x, y, result):
        self.calc.divide(x, y)
        self.calc.check_result_equals(result)

    def test_sign_change_display(self):
        self.calc.enter_number(-1)
        self.calc.check_result_equals("-1")

    def test_check_backspace(self):
        self.calc.enter_number(888)
        self.calc.backspace()
        self.calc.check_result_equals("88")

    def test_backspace_to_zero(self):
        self.calc.enter_number(88)
        self.calc.backspace()
        self.calc.backspace()
        self.calc.check_result_equals("0")

    def test_clear(self):
        self.calc.enter_number(111)
        self.calc.clear_entry()
        self.calc.check_result_equals("0")

    def test_display_equation(self):
        self.calc.enter_number(1)
        self.calc.tap_by_name(self.calc.minus_button_name)
        self.calc.enter_number(2)
        self.calc.check_result_equals("1\n-\n2")

    def test_clear_second_entry(self):
        self.calc.enter_number(2)
        self.calc.tap_by_name(self.calc.plus_button_name)
        self.calc.enter_number(3)
        self.calc.clear_entry()
        self.calc.check_result_equals("2\n+\n0")

    def test_clear_all(self):
        self.calc.enter_number(2)
        self.calc.clear_all()
        self.calc.check_result_equals("0")

    def test_clear_all_with_second_entry(self):
        self.calc.enter_number(2)
        self.calc.tap_by_name(self.calc.plus_button_name)
        self.calc.enter_number(3)
        self.calc.clear_all()
        self.calc.check_result_equals("0")

    @parameterized.expand([
        ("add_small_number", 1, "1E+11"),
        ("add_big_number", 100000, "1.000001E+11")
    ])
    def test_scientific_notation_repeated_sum(self, name, number, result):
        self.calc.multiply(10000000000, 10)
        self.calc.sum_result(number)
        self.calc.check_result_equals(result)

    @parameterized.expand([
        ("multiply", 10, "1E+12"),
        ("multiply_by_decimal_fraction", 0.1, "1E+10"),
        ("back_from_scientific_by_multiply_decimal_fraction", 0.000001, "100000")
    ])
    def test_scientific_notation_repeated_mul(self, name, number, result):
        self.calc.multiply(10000000000, 10)
        self.calc.multiply_result(number)
        self.calc.check_result_equals(result)


if __name__ == '__main__':
    unittest.main()
