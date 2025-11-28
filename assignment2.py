

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

# Main Search Operation
def run_search(students):
    """Handle the search process until the user enters -1 to return."""
    while True:
        student_id = input_int(
            "Enter the id of the student. Enter -1 to return to the previous menu: ",
            accept_neg1=True
        )

        if student_id == -1:
            return

        result = search(students, student_id)
        if result:
            print("Student found")
            print(student_id, result["name"], result["gpa"])
        else:
            print("Student not found")

# Main Edit Operation
def run_edit(students):
    """Allow the user to edit a student's name using their ID."""
    while True:
        student_id = input_int(
            "Enter the id of the student. Enter -1 to return to the previous menu: ",
            accept_neg1=True
        )

        if student_id == -1:
            return

        result = search(students, student_id)
        if not result:
            print("Student not found")
            continue

        new_name = input_nonempty("Enter the new name of the student: ")
        edit_name(students, student_id, new_name)

        print(f"Student name modified for the student with id {student_id}")
        print("Student's new name is", new_name)

# Main Remove Operation
def run_remove(students):
    """Remove students until the user chooses to stop."""
    while True:
        print("Enter id of the student that you want to remove from the students' registry.")
        student_id = input_int("id: ")

        if remove(students, student_id):
            print("Student removed")
        else:
            print("Student not found")

        again = input("Do you want to remove more students? y(yes)/n(no) ").strip().lower()
        if again not in ("y", "yes"):
            break