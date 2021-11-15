from dz04_func import *


def test_convert_to_miles():
    assert convert_to_miles(1000) == 621.4


def test_get_days():
    assert get_days(4) == 30


def test_get_factors():
    assert get_factors(10) == [1, 2, 5, 10]


def test_is_prime():
    assert is_prime(121) == False
