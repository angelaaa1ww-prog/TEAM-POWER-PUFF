# Author : Amani Angela
# Date : 23/02/2026 
# Program to define a Person class for a school management system   




from person import Person

class Student(Person):
    def __init__(self, student_id, name, course, phone):
        super().__init__(name, phone)
        self.student_id = student_id
        self.course = course

    def display_student(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Phone: {self.phone}")
        print("----------------------------")