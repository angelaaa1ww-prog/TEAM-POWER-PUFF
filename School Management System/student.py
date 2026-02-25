# Author : Amani Angela
# Date : 23/02/2026 
# Program to define a Person class for a school management system   

# student.py

from person import Person


class Student(Person):
    def __init__(self, first_name, last_name, phone, student_id, course):
        super().__init__(first_name, last_name, phone)
        self.student_id = student_id
        self.course = course

    def get_details(self):
        return (
            f"Name: {self.first_name} {self.last_name}\n"
            f"Phone: {self.phone}\n"
            f"Student ID: {self.student_id}\n"
            f"Course: {self.course}\n"
            f"{'-'*40}"
        )

    def assign_new_course(self, new_course):
        self.course = new_course




