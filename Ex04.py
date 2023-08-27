# Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# - шестизначный идентификационный номер
# - уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from datetime import datetime
from random import randint


class Person:
    def __init__(self,
                 name: str,
                 surname: str,
                 year_birth: int) -> None:
        self.name = name
        self.surname = surname
        self.__age = datetime.now().year - year_birth

    def birthday(self):
        self.__age += 1

    def full_name(self) -> str:
        return f'{self.name} {self.surname}'

    def age(self) -> int:
        return self.__age

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'

    def __add__(self, obj):
        return f'{self.name} += {obj.name}'


class Employee(Person):
    __LOWER_LIM = 100_000
    __UPPER_LIM = 999_999
    __LEVEL_DIV = 7

    def __init__(self,
                 name: str,
                 surname: str,
                 year_birth: int) -> None:
        super().__init__(name, surname, year_birth)
        self.id = randint(self.__LOWER_LIM,
                          self.__UPPER_LIM)
        self.level = sum(map(int, list(str(self.id)))) % self.__LEVEL_DIV


e1 = Employee('Vlad', 'Isaev', 980)
e2 = Employee('Alex', 'Smirnov', 981)
print(e1.id, e1.level)
print(e1.id, e1.level)
print(e1.full_name())
print(e1 + e2)
