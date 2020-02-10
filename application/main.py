from student import *
from university import *

def print_graduation():
 print("*****Full list University graduation******")
first_student = Students("Ivan Ivanov", 20)
first_student.years_of_student()
first = first_student.get_student()
print(first)



second_student = Students("Petyr Petrov",19)
third_student = Students("Radi Peev",21)
student_list = [first_student,second_student]
students_lis = University(student_list)
students_lis.add_student(third_student)

print_graduation()
students_lis.print_students_in_class()
