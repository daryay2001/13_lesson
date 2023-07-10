class Person:
    def __init__(self, name, age):
        self._name = "no name"  # берем protected, чтобы исп их в классах наследниках
        self._age = 18
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 2:
            self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 14:
            self._age = age

    def show_info(self):
        print(f"Name: {self._name}, age: {self._age}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self._subject = "No subject"
        self.subject = subject

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        if len(subject) > 1:
            self._subject = subject

    def teach(self):
        print(f"Teacher {self._name} can teach")

    def study(self):
        print(f"Teacher {self.name} is already graduated")

    def show_info(self):
        super().show_info()
        print(f"Subject: {self._subject}")



class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = 1
        self.grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade >= 1:
            self._grade = grade

    def teach(self):
        print(f"Student {self._name} can't teach")

    def study(self):
        print(f"Student {self.name} should study")

    def show_info(self):
        super().show_info()
        print(f"Grade: {self._grade}")

class Subject:
    def __init__(self, subject):
        self._subject = "no subject"
        self.subject = subject

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        if len(subject) >= 2:
            self._subject = subject


class Academy:
    def __init__(self, name):
        self._name = "Nevermore"
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 2:
            self._name = name

    def add_teachers(self, teacher):
        self.teachers.append(teacher)

    def add_students(self, student):
        self.students.append(student)

    def add_subjects(self, subject):
        self.subjects.append(subject)

    def show_info(self):
        print(f"Academy name: {self._name}")
        print(f"Academy teachers: ")  # Будем передавать красиво, а не просто списком
        for teacher in self.teachers:
            teacher.show_info()
            # print(teacher)

        print(f"List of the students: ")
        for student in self.students:
            student.show_info()
            # print(student)

        print(f"Subjects:")
        for subject in self.subjects:
            print(subject.subject)  # перепроверить, может быть subject.subject


class Dormitory(Academy):
    def __init__(self, name):
        super().__init__(name)
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)


class Room:
    def __init__(self, number, capacity):
        self.number = number
        self._capacity = 0
        self.capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity > 0:
            self._capacity = capacity


class Auditoriums(Academy):
    def __init__(self, name):
        super().__init__(name)
        self._human_capacity = 0

    @property
    def human_capacity(self):
        return self._human_capacity

    @human_capacity.setter
    def human_capacity(self, capacity):
        if capacity > 0:
            self._human_capacity = capacity


# def show_activities(people):
#     people.study()
#     people.teach()  # на этом этапе нам все равно какого типа будет экземпляр - интерфейс взаимодействия одинаковый
#
#
# myTeacher = Teacher("Mikky", 23, "Math")
# myStudent = Student("Kolya", 17, 3)
#
# show_activities(myTeacher)
# show_activities(myStudent)

english_teacher = Teacher("Kate Black", 32, "English")
math_teacher = Teacher("John Black", 33, "Math")
evil_teacher = Teacher("Sauron", 30000, "Dark Magic")

student_good = Student("Frodo Baggins", 30, 5)
student_good_2 = Student("Harry Potter", 15, 5)
student_bad = Student("Harley Quinn", 25, 3)

engl_subject = Subject("English")
math_subject = Subject("Mathematics")
evil_subject = Subject("Dark Magic")

academy = Academy("Evil Academy")

academy.add_teachers(english_teacher)
academy.add_teachers(math_teacher)
academy.add_teachers(evil_teacher)

academy.add_students(student_good)
academy.add_students(student_good_2)
academy.add_students(student_bad)

academy.add_subjects(engl_subject)
academy.add_subjects(math_subject)
academy.add_subjects(evil_subject)

room1 = Room("12B", 3)
room2 = Room("13", 13)

dormitory = Dormitory("Evil Academy Dormitory")
dormitory.add_room(room1)
dormitory.add_room(room2)

auditor = Auditoriums("Dark Auditorium")
auditor.human_capacity = 17

academy.show_info()

print("Dormitory info: ")
print(f"Dormitory name: {dormitory.name}")
for room in dormitory.rooms:
    print(f"room number: {room.number}, Capacity: {room.capacity}")

print("Auditorium info: ")
print(f"Auditorium name: {auditor.name}")
print(f"Human capacity: {auditor.human_capacity}")