# Author : Amani Angela
# Date : 23/02/2026 
# Program to define a Person class for a school management system


class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")

