# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

from datetime import datetime

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


p1 = Person('Vlad', 'Isaev', 980)
p2 = Person('Alex', 'Smirnov', 981)
print(p1.age())
print(p1.birthday())
print(p1.age())
print(p1.full_name())
print(p1)
print(p1 + p2)
