# Name : Angela Amani
# Date : 23/02/2026
# Program to define a Person class for a school management system

from student import Student
from openpyxl import Workbook

students = [] # global list


def register_student():
    print("\n--- Register New Student ---")

    student_id = input("Enter Student ID: ").strip()

    # Prevent duplicate IDs
    for s in students:
        if s.student_id == student_id:
            print("Student ID already exists!\n")
            return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course: ").strip()
    phone = input("Enter Phone Number: ").strip()

    new_student = Student(student_id, name, course, phone)
    students.append(new_student)

    print("Student registered successfully!\n")


def display_students():
    print("\n--- Students in System ---")

    if not students:
        print("No students registered.\n")
        return

    for student in students:
        student.display_student()


def assign_new_course():
    print("\n--- Assign New Course ---")
    student_id = input("Enter Student ID: ").strip()

    for student in students:
        if student.student_id == student_id:
            new_course = input("Enter New Course: ").strip()
            student.course = new_course
            print("Course updated successfully!\n")
            return

    print("Student not found.\n")


def export_to_excel():
    if not students:
        print("No data to export.\n")
        return

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Students"

    # Headers
    sheet.append(["ID", "Name", "Course", "Phone"])

    # Data
    for student in students:
        sheet.append([
            student.student_id,
            student.name,
            student.course,
            student.phone
        ])

    workbook.save("students.xlsx")
    print("Data exported to students.xlsx successfully!\n")


def main():
    while True:
        print("====== SCHOOL MANAGEMENT SYSTEM ======")
        print("1. Register New Student")
        print("2. Display Students")
        print("3. Assign New Course")
        print("4. Export to Excel")
        print("5. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            assign_new_course()
        elif choice == "4":
            export_to_excel()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()




