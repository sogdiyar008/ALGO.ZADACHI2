# class Student:
#     def __init__(self, name, age, average_grade):
#         self.name = name
#         self.age = age
#         self.average_grade = average_grade
#
#     def get_name(self):
#         print(self.name)
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_age(self):
#         print(self.age)
#
#     def set_age(self, age):
#         self.age = age
#
#     def get_average_grade(self):
#         print(self.average_grade)
#
#     def set_average_grade(self, average_grade):
#         self.average_grade = average_grade
#
#     def all_info(self):
#         print(f'''
# Имя студента: {self.name}
# Возраст студента: {self.age}
# Средний балл студента: {self.average_grade}''')
#
#
# student1 = Student("Согдияр", 16, 4.12)
# student1.all_info()
#
# student1.set_name("Петр")
# student1.set_age(21)
# student1.set_average_grade(4.8)
# student1.all_info()

#########################################
#222222222222222222222222222222222222222#
#########################################

# class Rectangle:
#     def __init__(self,width,length):
#         self.width=width
#         self.length=length
#
#     def perimeter(self):
#         print('периметр: ', (self.width+self.length)*2)
#
#     def area(self):
#         print('площадь: ', self.length*self.width)
#
# rectangle =Rectangle(2,5)
# rectangle.area()
# rectangle.perimeter()

#############################
#333333333333333333333333333#
#############################

# class Car:
#     def __init__(self, mark, model, year_of_issue, mileage):
#         self.mark = mark
#         self.model = model
#         self.year_of_issue = year_of_issue
#         self.mileage = mileage
#
#     def set_mark(self, new_mark):
#         self.mark = new_mark
#
#     def set_model(self, new_modelnew_year_of_issue):
#         self.model = new_modelnew_year_of_issue
#
#     def set_year_issue(self, new_year_of_issue):
#         self.year_of_issue = new_year_of_issue
#
#     def set_mileage(self, new_mileage):
#         self.mileage = new_mileage
#
#     def all_info(self):
#         return f"Автомобиль: {self.mark} {self.model}, Год выпуска: {self.year_of_issue}, Пробег: {self.mileage} км"
#
# # Пример использования класса "Автомобиль":
# car = Car("Toyota", "Camry", 2020, 25000)
# print(car.all_info())  # Вывод информации об автомобиле
#
# # Изменяем значения атрибутов
# car.set_mark("Honda")
# car.set_year_issue(2022)
# car.set_mileage(15000)
#
# # Вывод обновленной информации
# print(car.all_info())



################################
#444444444444444444444444444444#
################################

# class BankAccount:
#     def __init__(self,balance,interest_rate):
#         self.__balance=balance
#         self.__interest_rate=interest_rate
#         self.__transactions=[]
#         print('Добавлен пользователь со счетом ',self.__balance ,'и процентной ставкой в',self.__interest_rate, '%')
#
#
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             self.__transactions.append(f"Внесение наличных на счет: {amount}")
#         else:
#             return "депозит не может быть меньше 0"
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             self.__transactions.append(f"Снятие наличных: {amount}")
#         else:
#             return 'Нельзя отнять  меньше чем 0 и больше чем баланс'
#
#     def add_interest(self):
#         interest_amount = self.__balance * self.__interest_rate
#         self.__balance += interest_amount
#         self.__transactions.append(f"Добавлены проценты  ({self.__interest_rate}), что состовляет {interest_amount}")
#
#     def history(self):
#         for transaction in self.__transactions:
#             print(transaction)
#
#     def get_balance(self):
#         print('ваш баланс состовляет: ',self.__balance)
#
#
# # создаем объект счета с балансом 100000 и процентом по вкладу 0.05
# account = BankAccount(100000, 0.05)
#
# # вносим 15 тысяч на счет
# account.deposit(15000)
#
# # снимаем 7500 рублей
# account.withdraw(7500)
#
# # начисляем проценты по вкладу
# account.add_interest()
#
# # печатаем историю
# account.history()
#
# # смотрим баланс
# account.get_balance()


####################
#555555555555555555#
####################


# class Triangle:
#     def __init__(self, side1, side2, side3):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#
#     def triangle_type(self):
#         if self.side1 == self.side2 == self.side3:
#             print("Треугольник у вас равносторонний")
#         elif self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3:
#             print("Треугольник у вас равнобедренный")
#         else:
#             print("Треугольник у вас разносторонний")
#
#     def calculate_area(self):
#         s = (self.side1 + self.side2 + self.side3) / 2
#         return (s * (s - self.side1) * (s - self.side2) * (s - self.side3))**0.5
#
# triangle1=Triangle(5,5,5)
# triangle1.triangle_type()
#
# triangle2=Triangle(5,5,6)
# triangle2.triangle_type()
#
# triangle3=Triangle(4,5,6)
# triangle3.triangle_type()