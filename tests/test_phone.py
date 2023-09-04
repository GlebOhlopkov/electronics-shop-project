import pytest
from src.phone import Phone


@pytest.fixture()
def test_item():
    return Phone('Nokia', 1000, 5, 1)


def test__repr__(test_item):
    assert test_item.__repr__() == "Phone('Nokia', 1000, 5, 1)"


def test__str__(test_item):
    assert test_item.__str__() == 'Nokia'


def test__add__(test_item):
    assert test_item.__add__(Phone('IPhone',20000, 50, 2)) == 55


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 5000


def test_apply_discount(test_item):
    test_item.pay_rate = 1.5
    test_item.apply_discount()
    assert test_item.price == 1500


def test_name(test_item):
    test_item.name = 'Sumsung'
    assert test_item.name == 'Sumsung'


def test_name(test_item):
    test_item.name = 'SuperSumsung'
    assert test_item.name == 'SuperSumsu'


def test_string_to_number(test_item):
    assert test_item.string_to_number('10.0') == 10
