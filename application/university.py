from student import *


class University:
    def __init__(self, student_list):
        self.student_list = student_list

    def print_students_in_class(self):
        for student in self.student_list:
            print (student.get_student())

    def add_student(self, student):
        self.student_list.append(student)
