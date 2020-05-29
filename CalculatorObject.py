from altunityrunner import By


class CalculatorObject:
    clear_entry_button_name = "ClearEntry"
    plus_button_name = "Plus"
    clear_all_button_name = "ClearAll"
    multiply_button_name = "Multiplication"
    negative_button_name = "ChangeSign"
    equals_button_name = "Equals"
    divide_button_name = "Division"
    dot_button_name = "Point"
    erase_last_button_name = "EraseSymbol"
    minus_button_name = "Minus"
    display_name = "Text"

    def __init__(self, unity_driver):
        self.unity_driver = unity_driver

    def tap_by_name(self, name):
        self.unity_driver.find_object(By.NAME, name).tap()

    def enter_number(self, number):
        change_sign = False
        if number % 1 != 0:
            str_number = str('%f' % number)
        else:
            str_number = str(number)
        for char in str(str_number):
            if char == "-":
                change_sign = True
            elif char == ".":
                self.tap_by_name(self.dot_button_name)
            else:
                self.tap_by_name(char)
        if change_sign:
            self.tap_by_name(self.negative_button_name)

    def change_sign(self):
        self.tap_by_name(self.negative_button_name)

    def backspace(self):
        self.tap_by_name(self.erase_last_button_name)

    def clear_entry(self):
        self.tap_by_name(self.clear_entry_button_name)

    def clear_all(self):
        self.tap_by_name(self.clear_all_button_name)

    def sum(self, x, y):
        self.enter_number(x)
        self.tap_by_name(self.plus_button_name)
        self.enter_number(y)
        self.tap_by_name(self.equals_button_name)

    def subtract(self, x, y):
        self.enter_number(x)
        self.tap_by_name(self.minus_button_name)
        self.enter_number(y)
        self.tap_by_name(self.equals_button_name)

    def multiply(self, x, y):
        self.enter_number(x)
        self.tap_by_name(self.multiply_button_name)
        self.enter_number(y)
        self.tap_by_name(self.equals_button_name)

    def divide(self, x, y):
        self.enter_number(x)
        self.tap_by_name(self.divide_button_name)
        self.enter_number(y)
        self.tap_by_name(self.equals_button_name)

    def sum_result(self, x):
        self.tap_by_name(self.plus_button_name)
        self.enter_number(x)
        self.tap_by_name(self.equals_button_name)

    def subtract_result(self, x):
        self.tap_by_name(self.minus_button_name)
        self.enter_number(x)
        self.tap_by_name(self.equals_button_name)

    def multiply_result(self, x):
        self.tap_by_name(self.multiply_button_name)
        self.enter_number(x)
        self.tap_by_name(self.equals_button_name)

    def divide_result(self, x):
        self.tap_by_name(self.divide_button_name)
        self.enter_number(x)
        self.tap_by_name(self.equals_button_name)

    def check_result_equals(self, text):
        if "\n" not in text:
            text += "\n\n"
        assert self.unity_driver.find_object(By.NAME, self.display_name).get_text() == text
