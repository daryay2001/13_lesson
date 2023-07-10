# class Person:
#     def __init__(self, age):
#         self.__age = age
#
#     # @staticmethod
#     def show(self):
#         print(self.__age)
#
#     def __secret_info(self):
#         print("secret_info")
#         print(self.__age)


# vasya = Person(33)
# print(vasya.__age)
# vasya.__age = 44  # под капотом мы просто создаем новое поле которое не имеет никакого отношения к
# # к полю  self.__age из класса
# print(vasya.__age)
# vasya.show()
#
# petya = Person(55)
# petya.__secret_info()
# petya._Person__secret_info()  # это ломает инкапсуляцию и так делать не надо!
#
# Person.show(petya)

# v2 реализация инкапсуляции через аннотацию свойств

# class User:
#     __name: str = "no name"  # private поле, доступно только внутри этого класса
#     __age: int = 0
#     __secret: int = 12345
#
#     def __init__(self, name, age):
#         # self.__name = name
#         # self.__age = age
#         # применим инкапсуляцию
#         self.name = name
#         self.age = age
#
#     # getter - для получения значения приватного поля
#     @property
#     def name(self):
#         return self.__name
#
#     # setter - для санкционированного доступа к приватной переменной (полю)
#     @name.setter
#     def name(self, name):
#         if 2 < len(name) < 50:
#             self.__name = name
#         else:
#             print("Incorrect name length!")
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 18 < age < 150:
#             self.__age = age
#         else:
#             print("Incorrect age!")
#
#     def show_info(self):
#         print(f"Name: {self.__name} age: {self.__age}")
#         # self.__secret_info()
#
#     def __secret_info(self):
#         print(f"Secret code: {self.__secret}")
# #
# #
# vasya = User("Vasya", 44)
# vasya.show_info()
# print(vasya.name)  # отработает getter
# vasya.name = "Vasek"  # отработает setter
# print(vasya.name)

##
# class MyConverter:
#     __money_sum = 0
#     __grn_rate = 37.6
#
#     def __init__(self, input_money):
#         self.money_sum = input_money
#
#     @property
#     def money_sum(self):
#         return self.__money_sum
#
#     @money_sum.setter
#     def money_sum(self, input_sum):
#         if 100 < input_sum < 100000:
#             self.__money_sum = input_sum
#         else:
#             print("Provide valid money sum in grn")
#
#     # readonly property
#     @property
#     def grn_rate(self):
#         return self.__grn_rate
#
#     def show_grn_rate(self):
#         print(f"Current grn rate: {self.__grn_rate}")
#
#     def get_dollars_sum(self):
#         return self.__money_sum / self.__grn_rate
#
#
# conv = MyConverter(5000)
# conv.show_grn_rate()
# print("Result: ", round(conv.get_dollars_sum())) # Будет 133, но точнее 132,98
# conv_2 = MyConverter(99)
# print("Result: ", round(conv_2.get_dollars_sum()))


#############
# наследование
# v1
# class Person:
#     __name = "noname"
#     __age = 18
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__secret = 12345  # (private) -> доступ только внутри класса
#         self._hobby = "no info"  # (protected) -> доступ внутри класса и в классах наследниках
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if len(name) > 2:
#             self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age > 18:
#             self.__age = age
#
#     @property
#     def hobby(self):
#         return self._hobby
#
#     @hobby.setter
#     def hobby(self, hobby):
#         if len(hobby) > 0:
#             self._hobby = hobby
#
#     def show_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# class Employee(Person):  # наследуемся от класса Person
#     def work(self):
#         print(f"{self.name} works!")
#         # print(self.__secret)  # AttributeError: 'Employee' object has no attribute '_Employee__secret'
#         print(self._hobby)  # есть доступ так как в базовом классе это поле protected
# #
# #
# vasya = Employee("Vasya", 33)
# vasya.show_info()
# vasya.work()
# #
# # print(vasya._hobby)  # к protected полям не стоит обращаться напрямую, лучше использовать геттер
# print(vasya.hobby)
# vasya.hobby = "test"
# print(vasya.hobby)

##
# v2
# class Person:
#     __name = "noname"
#     __age = 18
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__secret = 12345  # (private) -> доступ только внутри класса
#         self._hobby = "no info"  # (protected) -> доступ внутри класса и в классах наследниках
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if len(name) > 2:
#             self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age > 18:
#             self.__age = age
#
#     @property
#     def hobby(self):
#         return self._hobby
#
#     def show_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# class Employee(Person):  # наследуемся от класса Person
#     def __init__(self, name, age, company):
#         # v1
#         super().__init__(name, age)  # вызов конструктора базового класса Person
#         # super() -> ссылка на базовый класс, получаем доступ к элементам базового класса
#         # v2
#         # Person.__init__(self, name, age)
#         self.company = company
#
#     def work(self):
#         print(f"{self.name} works in {self.company} company")
#         # print(self.__secret)  # AttributeError: 'Employee' object has no attribute '_Employee__secret'
#         print(self._hobby)  # есть доступ так как в базовом классе это поле protected
#         # print(super().show_info())
#         # print(super().name)
#
#     # переопределение метода
#     def show_info(self):
#         super().show_info()  # вызов метода базового класса
#         print(f"Works in {self.company} company")  # расширили своей логикой
#
#
# vasya = Employee("Vasya", 33, "Google")
# vasya.show_info()
# vasya.work()

##############
###
# v3
# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#     def work(self):
#         print(f"{self.name} works!")
#
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def study(self):
#         print(f"{self.name} studies!")
#
#
# class WorkingStudent(Student, Employee):  # множественное наследование
#     pass
#
#
# vasya = WorkingStudent("Vasya")
# vasya.work()
# vasya.study()
# print(WorkingStudent.mro())
# # [<class '__main__.WorkingStudent'>, <class '__main__.Student'>, <class '__main__.Employee'>, <class 'object'>]

##
# v4 пример ромбовидного наследования # Добавила инкапсуляцию, работает
# class Person:
#     __name = "no name"
#     __age = 18
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, name):
#         if len(name) > 2:
#             self.__name = name
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if age >= 18:
#             self.__age = age
#
#     def show_info(self):
#         print(f"Name: {self.name}\nAge: {self.age}")
#
#
# class Employee(Person):
#     def __init__(self, name, age, company="Point"):
#         super().__init__(name, age)
#         self.__company = "Point"
#         self.company = company
#
#     @property
#     def company(self):
#         return self.__company
#
#     @company.setter
#     def company(self, company):
#         if len(company) > 2:
#             self.__company = company
#
#
#     def show_info(self):
#         super().show_info()
#         print(f"Company: {self.company}")
#
#
# class Student(Person):
#     def __init__(self, name, age, university="Harvard"):
#         super().__init__(name, age)
#         self.__university = "Harvard"
#         self.university = university
#     @property
#     def university(self):
#         return self.__university
#     @university.setter
#     def university(self, university):
#         if len(university) > 2:
#             self.__university = university
#
#     def show_info(self):
#         super().show_info()
#         print(f"University: {self.university}")
#
#
# class WorkingStudent(Employee, Student):
#     def __init__(self, name, age, company, university):
#         Employee.__init__(self, name, age, company)
#         Student.__init__(self, name, age, university)
#
#
#     def show_info(self):
#         super().show_info()
#         # Student.show_info(self)
#         # Employee.show_info(self)
# #
# #
# vasya = WorkingStudent("Vasya", 33, "Google", "Tech")
# # vasya.show_info()
# # print(vasya.company)
# # print(vasya.university)
# # print(WorkingStudent.mro())
# kolya = WorkingStudent("Kolya", 12, "i", "e")
# kolya.show_info()

##
# https://makina-corpus.com/python/python-tutorial-understanding-python-mro-class-search-path
# http://www.srikanthtechnologies.com/blog/python/mro.aspx

##############
####
# добавить инкапсуляцию - добавила, работает
# class Transport:
#     __name = "no name"
#     __year = 2001
#
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if len(name) > 2:
#             self.__name = name
#
#     @property
#     def year(self):
#         return self.__year
#
#     @year.setter
#     def year(self, year):
#         if year > 1950:
#             self.__year = year
#
#     def show_info(self):
#         print(f"Name: {self.name}\nyear: {self.year}")
#
#
# class BaseAuto(Transport):
#     def __init__(self, name, year, wheels_count=0):
#         super().__init__(name, year)
#         self.__wheels_count = 0
#         self.wheels_count = wheels_count
#
#     @property
#     def wheels_count(self):
#         return self.__wheels_count
#
#     @wheels_count.setter
#     def wheels_count(self, wheels_count):
#         if wheels_count > 0:
#             self.__wheels_count = wheels_count
#
#     # перекрытие метода базового класса Transport
#     def show_info(self):
#         print(f"Wheels count: {self.wheels_count}")
#
#
# class WaterTransport(Transport):
#     def __init__(self, name, year, displacement=0.):
#         super().__init__(name, year)
#         self.__displacement = 0
#         self.displacement = displacement
#
#     @property
#     def displacement(self):
#         return self.__displacement
#
#     @displacement.setter
#     def displacement(self, displacement):
#         if displacement > 0:
#             self.__displacement = displacement
#
#     # перекрытие метода базового класса Transport
#     def show_info(self):
#         print(f"Displacement: {self.displacement}")
#
#
# class Auto(BaseAuto):
#     def __init__(self, name, year, wheels_count, machine_body_form_factor):
#         super().__init__(name, year, wheels_count)
#         self.machine_body_form_factor = machine_body_form_factor
#
#     # перекрытие метода базового класса BaseAuto
#     def show_info(self):
#         print(f"Machine body form factor: {self.machine_body_form_factor}")
#
#
# class Amphibian(WaterTransport, BaseAuto):
#     def __init__(self, name, year, wheels_count, displacement):
#         WaterTransport.__init__(self, name, year, displacement)
#         BaseAuto.__init__(self, name, year, wheels_count)
#
#     # переопределение метода show_info
#     def show_info(self):
#         Transport.show_info(self)
#         WaterTransport.show_info(self)
#         BaseAuto.show_info(self)
#
#
# test_car = Amphibian("BMW", 2023, 4, 123.2)
# test_car.show_info()
# print(Amphibian.mro())
# another_car = Amphibian("Reka_more", 1951, 5, 1234)
# another_car.show_info()

################################
# полиморфизм
# https://maxdrive.kyiv.ua/dokumentacija/pochta/chto-takoe-polimorfizm-v-python

# class Parrot:
#     __name = "Kesha"
#
#     def fly(self):
#         print(f"Parrot {self.__name} can fly")
#
#     def swim(self):
#         print(f"Parrot {self.__name} can't swim")
#
#
# class Penguin:
#     __name = "Bobik"
#
#     def fly(self):
#         print(f"Penguin {self.__name} can't fly")
#
#     def swim(self):
#         print(f"Penguin {self.__name} can swim")
#
#
# # общий интерфейс
# def show_animal_info(bird):
#     # на этом этапе нам все равно какого типа будет экземпляр - интерфейс взаимодействия одинаковый: fly and swim
#     bird.fly()
#     bird.swim()
#
#
# # создаем объекты
# my_parrot = Parrot()
# my_penguin = Penguin()
#
# # передадим в общий интерфейс экземпляры
# show_animal_info(my_parrot)
# show_animal_info(my_penguin)
