"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def test_item():
    return Item('TV', 5000, 10)


def test__repr__(test_item):
    assert test_item.__repr__() == 'Item(TV, 5000, 10)'


def test__str__(test_item):
    assert test_item.__str__() == 'TV'


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 50000


def test_apply_discount(test_item):
    test_item.pay_rate = 1.5
    test_item.apply_discount()
    assert test_item.price == 7500


def test_name(test_item):
    test_item.name = 'Notebook'
    assert test_item.name == 'Notebook'


def test_name(test_item):
    test_item.name = 'SuperNotebook'
    assert test_item.name == 'SuperNoteb'


def test_string_to_number(test_item):
    assert test_item.string_to_number('10.0') == 10
