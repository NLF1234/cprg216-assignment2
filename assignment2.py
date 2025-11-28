

from functions import (
    input_int,
    input_float,
    input_nonempty,
    search,
    add,
    remove,
    edit_name,
)

# Main Add Operation
def run_add(students):
    """Handle adding new students through repeated user prompts."""
    print("Enter id of the student, followed by the student's information.")
    while True:
        student_id = input_int("id: ")
        name = input_nonempty("name: ")
        gpa = input_float("gpa: ", 0.0, 4.0)
        semester = input_int("semester: ")

        add(students, student_id, name, gpa, semester)
        print("Student added")
        print(student_id, name, gpa, semester)

        again = input("Do you want to add a new student? y(yes)/n(no) ").strip().lower()
        if again not in ("y", "yes"):
            break


