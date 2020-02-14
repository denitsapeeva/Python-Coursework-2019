from student import *
from university import *


def print_graduation():
 print("*****Full list University graduation******")


first_student = Students("Ivan Ivanov", 20)
first_student.years_of_student()
years_of_graduation = first_student.get_graduates()
print(years_of_graduation)


def print_who_is_excluded():
 print("*****Full list of Excluded students******")


def excluded_students():
 excluded_student = Students('Georgi Georgiev',44)
 print(excluded_student.name_of_student + " is " + str(excluded_student.year) + " years old and he is excluded!")


second_student = Students("Petyr Petrov",19)
third_student = Students("Radi Peev",21)
student_list = [first_student,second_student,third_student]
all_students = University(student_list)



print_graduation()
all_students.print_students_in_class()
print_who_is_excluded()
excluded_students()
