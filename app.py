from mymodules.models import Student
from mymodules.math_utils import average_grade

def main():
    s1 = Student("Ryan", 95)
    s2 = Student("Alex", 90)
    s3 = Student("Bob", 86)
    s4 = Student("Chris", 82)
    s5 = Student("Dale", 78)
    s6 = Student("Eric", 74)
    s7 = Student("Fred", 76)
    s8 = Student("Greg", 80)
    s9 = Student("Han", 84)
    s10 = Student("Ivan", 88)
    roster = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
    for i in range(10):
        roster[i].print_student_info()
    result = average_grade(roster)
    print(f"Average Grade: {result}")

if __name__ == "__main__":
    main()
