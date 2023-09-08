import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def test_item():
    return Keyboard('LOGITECH', 10000, 5)


def test__repr__(test_item):
    assert test_item.__repr__() == "Keyboard('LOGITECH', 10000, 5)"


def test__str__(test_item):
    assert test_item.__str__() == 'LOGITECH'


def test__add__(test_item):
    assert test_item.__add__(Keyboard('RAZER',50000, 10)) == 15


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 50000


def test_apply_discount(test_item):
    test_item.pay_rate = 1.5
    test_item.apply_discount()
    assert test_item.price == 15000


def test_name(test_item):
    test_item.name = 'ASUS'
    assert test_item.name == 'ASUS'


def test_name(test_item):
    test_item.name = 'Steelseries'
    assert test_item.name == 'Steelserie'


def test_string_to_number(test_item):
    assert test_item.string_to_number('10.0') == 10
