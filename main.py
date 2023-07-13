# Task 1
class Item:

    def __init__(self, name, shop, price):
        self.__name = name
        self.__shop = shop
        self.__price = price

    def get_get_name(self):
        return self.__name

    def get_shop(self):
        return self.__shop

    def get_price(self):
        return self.__price


class Storage:

    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def get_item_by_index(self, index):
        if index < 0 or index >= len(self.__items):
            return None
        return self.__items[index]

    def get_item_by_name(self, name):
        for item in self.__items:
            if item.get_name() == name:
                return item
        return None

    def sort_by_name(self):
        self.__items.sort(key=lambda x: x.get_name())

    def sort_by_shop(self):
        self.__items.sort(key=lambda x: x.get_shop())

    def sort_by_price(self):
        self.__items.sort(key=lambda x: x.get_price())

    def __add__(self, other):
        if isinstance(other, Storage):
            new_store = Storage()
            new_store.__items = self.__items + other.__items
            return new_store
        elif isinstance(other, Item):
            new_store = Storage()
            new_store.__items = self.__items + [other]
            return new_store
        else:
            return None
