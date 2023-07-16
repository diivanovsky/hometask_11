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


# 2 Task
class BeeElephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        if self.bee >= self.elephant:
            return True
        return False

    def trumpet(self):
        if self.bee <= self.elephant:
            return 'tu-tu-doo-doo!'
        return 'bzzzzzz'

    def eat(self, meal, value):
        if meal == 'nectar':
            self.bee += value
            self.elephant -= value
        elif meal == 'grass':
            self.bee -= value
            self.elephant += value
        if self.elephant > 100:
            self.elephant = 100
        elif self.elephant < 0:
            self.elephant = 0
        if self.bee > 100:
            self.bee = 100
        elif self.bee < 0:
            self.bee = 0
        return f"Bee's part is {self.bee} and elephant's part is {self.elephant}"


# 3 Task

class Bus:
    def __init__(self, speed, max_seats, max_speed):
        self.speed = speed
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = []
        self.free_seats = True
        self.seats = {}

    def add_passenger(self, *passenger_names):
        if len(self.passengers) + len(passenger_names) > self.max_seats:
            print("No seats available")
            return
        for name in passenger_names:
            self.passengers.append(name)
        self.update_seats()

    def remove_passenger(self, *passenger_names):
        for name in passenger_names:
            if name in self.passengers:
                self.passengers.remove(name)
        self.update_seats()

    def increase_speed(self, value):
        if self.speed + value > self.max_speed:
            print("Overcome speed limit")
            return
        self.speed += value

    def decrease_speed(self, value):
        if self.speed - value < 0:
            print("Speed can't be below zero")
            return
        self.speed -= value

    def update_seats(self):
        self.seats = {i: name for i, name in enumerate(self.passengers, start=1)}
        if len(self.passengers) == self.max_seats:
            self.free_seats = False
        else:
            self.free_seats = True
