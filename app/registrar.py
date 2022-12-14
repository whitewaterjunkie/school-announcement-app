from person import *
from registrarAdmin import *
from Student import *
from UniversityPresident import *
from UniversitySecretary import *
from singleton import *
from abc import abstractmethod
from announcement import *


class Registrar(metaclass=Singleton):
    def __init__(self) -> None:
        self.__students = []
        self.am = AnnouncementManager()

    def add_student(self, student):
        self.__students.append(student)
        self.am.attach(student)

    def add_multiple_students(self, *args):
        for s in args:
            self.__students.append(s)
            self.am.attach(s)

    def remove_student(self, student):
        self.__students.remove(student)
        self.am.detach(student)

    def get_students_list(self) -> list:
        return self.__students

    def get_students(self):
        print("\nStudents: \n[ID]:")
        print(" \n".join(["["+str(i) + "] " + student.getName() + f" [{student.get_type()}]" for i,
                          student in enumerate(self.__students)]))
        print("\n")

    def get_students_by_type(self, type):
        print(f"\n{type.name} Students: ")
        print(" \n".join(["["+str(i) + ") " + student.getName() + f" [{student.get_type()}]" for i,
                          student in enumerate(self.__students) if student.type == type.name]))
        print("\n")
