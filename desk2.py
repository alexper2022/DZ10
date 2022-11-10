"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
from os import system, name as osname


def cls():
    system('cls' if osname == 'nt' else 'clear')


pos_list = ['Директор', 'Администратор', 'Водитель', 'Работник']


class Position_check:

    def __set__(self, instance, value):
        if value not in pos_list:
            raise ValueError("Значение не входит в список должностей!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    position = Position_check()
    wage = NonNegative()
    bonus = NonNegative()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return (f"{self.name} {self.surname}")

    def get_total_income(self):
        return (self._income["wage"]+self._income["bonus"])


cls()
boss = Position("Николай", "Петров", "Директор", 100000, 50000)
print(f"Фамилия и Имя: {boss.get_full_name()}")
print(f"Должность: {boss.position}")
print(f"Зарплата + бонусы: {boss.get_total_income()}\n")

admin = Position("Василий", "Андреев", "Администратор", 50000, 15000)
print(f"Фамилия и Имя: {admin.get_full_name()}")
print(f"Должность: {admin.position}")
print(f"Зарплата + бонусы: {admin.get_total_income()}\n")

driver = Position("Алескандр", "Андреев", "Водитель", 35000, 10000)
print(f"Фамилия и Имя: {driver.get_full_name()}")
print(f"Должность: {driver.position}")
print(f"Зарплата + бонусы: {driver.get_total_income()}\n")

worker = Position("Михаил", "Еремин", "Работник", 10000, 5000)
print(f"Фамилия и Имя: {worker.get_full_name()}")
print(f"Должность: {worker.position}")
print(f"Зарплата + бонусы: {worker.get_total_income()}\n")

laborer0 = Position("Иван", "Иванов", "Работник", 7000, 2000)
print(f"Фамилия и Имя: {laborer0.get_full_name()}")
print(f"Должность: {laborer0.position}")
print(f"Зарплата + бонусы: {laborer0.get_total_income()}\n")

laborer1 = Position("Вася", "Пупкин", "Разнорабочий", 7000, 2000)
print(f"Фамилия и Имя: {laborer1.get_full_name()}")
print(f"Должность: {laborer1.position}")
print(f"Зарплата + бонусы: {laborer1.get_total_income()}\n")
