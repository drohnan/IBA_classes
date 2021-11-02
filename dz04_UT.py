import unittest
import dz04_func


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Тестирование началось")


    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("Тестирование закончилось")

    def setUp(self):
        """Set Up Method!"""
        print("Запуск теста")
        print("[" + self.shortDescription() + "]")

    def tearDown(self):
        """Tear Down Method!"""
        print("Подчищаем после [" + self.shortDescription() + "]")
        print()

    def test_convert_to_miles(self):
        """Переводит километры в мили"""
        self.assertEqual(dz04_func.convert_to_miles(1000), 621.4)  # 0.6214 * 1k == 621.4

    def test_get_days(self):
        """Возвращает количество дней в месяце"""
        self.assertEqual(dz04_func.get_days(4), 30)  # 4 - April - 30 days

    def test_get_factors(self):
        """Выводит список делителей числа"""
        self.assertEqual(dz04_func.get_factors(10), [1, 2, 5, 10])  # 10 делится без остатка на  1, 2, 5 и 10

    def test_is_prime(self):
        """Проверяет, является ли число простым"""
        self.assertFalse(dz04_func.is_prime(121))  # 121 - не простое число, делится на 11


if __name__ == '__main__':
    unittest.main()
