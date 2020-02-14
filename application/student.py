class Students:
  def __init__(self,name_of_student,years):
    self.name_of_student = name_of_student;
    self.year = years;

  def get_graduates(self):
    return self.name_of_student + " will be "+str(4+self.year)+" years old, when he graduates!"
  def years_of_student(self):
    print (self.name_of_student + " is " + str(self.year) + " years old!")



