# Name : TEAM POWER PUFF
# Date :24/02/2026
# Progrma to run a school management system

# main.py

import customtkinter as ctk
from tkinter import messagebox
from student import Student

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SchoolApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TEAM POWER PUFF SCHOOL MANAGEMENT SYSTEM")
        self.state("zoomed")  # Maximized with Min, Max, Close buttons

        self.students = []

        # Title Label
        self.title_label = ctk.CTkLabel(
            self,
            text="TEAM POWER PUFF SCHOOL MANAGEMENT SYSTEM",
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=20)

        # ---------------- INPUT FRAME ----------------
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(pady=10)

        self.entry_first = ctk.CTkEntry(self.input_frame, placeholder_text="First Name", width=200)
        self.entry_first.grid(row=0, column=0, padx=15, pady=10)

        self.entry_last = ctk.CTkEntry(self.input_frame, placeholder_text="Last Name", width=200)
        self.entry_last.grid(row=0, column=1, padx=15, pady=10)

        self.entry_phone = ctk.CTkEntry(self.input_frame, placeholder_text="Phone", width=200)
        self.entry_phone.grid(row=1, column=0, padx=15, pady=10)

        self.entry_id = ctk.CTkEntry(self.input_frame, placeholder_text="Student ID", width=200)
        self.entry_id.grid(row=1, column=1, padx=15, pady=10)

        self.entry_course = ctk.CTkEntry(self.input_frame, placeholder_text="Course", width=420)
        self.entry_course.grid(row=2, column=0, columnspan=2, padx=15, pady=10)

        # ---------------- BUTTON FRAME ----------------
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=20)

        self.register_btn = ctk.CTkButton(
            self.button_frame,
            text="Register Student",
            command=self.register_student,
            width=180
        )
        self.register_btn.grid(row=0, column=0, padx=15, pady=10)

        self.assign_btn = ctk.CTkButton(
            self.button_frame,
            text="Assign New Course",
            command=self.assign_course,
            width=180
        )
        self.assign_btn.grid(row=0, column=1, padx=15, pady=10)

        self.display_btn = ctk.CTkButton(
            self.button_frame,
            text="Display Student Info",
            command=self.display_students,
            width=180
        )
        self.display_btn.grid(row=0, column=2, padx=15, pady=10)

        self.exit_btn = ctk.CTkButton(
            self.button_frame,
            text="Exit",
            fg_color="red",
            hover_color="#8B0000",
            command=self.destroy,
            width=120
        )
        self.exit_btn.grid(row=0, column=3, padx=15, pady=10)

        # ---------------- DISPLAY BOX ----------------
        self.display_box = ctk.CTkTextbox(self, width=900, height=400)
        self.display_box.pack(pady=20)

    # ---------------- FUNCTIONS ----------------

    def register_student(self):
        fn = self.entry_first.get()
        ln = self.entry_last.get()
        phone = self.entry_phone.get()
        sid = self.entry_id.get()
        course = self.entry_course.get()

        if not fn or not ln or not phone or not sid or not course:
            messagebox.showerror("Error", "All fields are required")
            return

        student = Student(fn, ln, phone, sid, course)
        self.students.append(student)

        messagebox.showinfo("Success", "Student Registered Successfully")
        self.clear_entries()

    def assign_course(self):
        sid = self.entry_id.get()
        new_course = self.entry_course.get()

        if not sid or not new_course:
            messagebox.showerror("Error", "Enter Student ID and New Course")
            return

        for student in self.students:
            if student.student_id == sid:
                student.assign_new_course(new_course)
                messagebox.showinfo("Updated", "Course Updated Successfully")
                return

        messagebox.showerror("Error", "Student Not Found")

    def display_students(self):
        self.display_box.delete("1.0", "end")

        if not self.students:
            self.display_box.insert("end", "No students registered.\n")
            return

        for student in self.students:
            self.display_box.insert("end", student.get_details() + "\n")

    def clear_entries(self):
        self.entry_first.delete(0, "end")
        self.entry_last.delete(0, "end")
        self.entry_phone.delete(0, "end")
        self.entry_id.delete(0, "end")
        self.entry_course.delete(0, "end")

def save_to_file(self):
    try:
        with open("students.txt", "w") as file:
            file.write("TEAM POWER PUFF SCHOOL MANAGEMENT SYSTEM\n")
            file.write("=" * 50 + "\n\n")

            for student in self.students:
                file.write(f"Student ID : {student.student_id}\n")
                file.write(f"Name       : {student.get_full_name()}\n")
                file.write(f"Course     : {student.course}\n")
                file.write("-" * 50 + "\n")

    except Exception as e:
        print("Error saving file:", e)

if __name__ == "__main__":
    app = SchoolApp()
    app.mainloop()



