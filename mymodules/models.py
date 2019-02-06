

class Student:
    def __init__(self, student_name="", student_grade=0): #initialization fucntion
        self.student_name = student_name
        self.student_grade = student_grade
    def set_grade(grade):
        self.student_grade = grade
    def get_grade(self):
        return self.student_grade
    def print_student_info(self):
        print("Name: " + self.student_name + "\nGrade: " + str(self.student_grade) + "\n")
