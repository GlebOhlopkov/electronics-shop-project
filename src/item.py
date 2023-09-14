import csv
import os


class CSVNotFound(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Отсутствует файл типа .csv'

    def __str__(self):
        return self.message


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл items.csv поврежден'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
            return self.__name
        else:
            self.__name = name
            return self.__name

    @classmethod
    def instantiate_from_csv(cls):
        try:
            csv_file = os.path.exists('../src/items.csv')
            if not csv_file:
                raise CSVNotFound

            with open(csv_file, newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row.split(',')) < 3:
                        raise InstantiateCSVError
                    cls(row['name'], row['price'], row['quantity'])

        except CSVNotFound as found_error:
            print(found_error)
        except InstantiateCSVError as file_error:
            print(file_error)


    @staticmethod
    def string_to_number(any_string):
        return int(float(any_string))
