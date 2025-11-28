"""
Assignment 2 – Student Record Program
Authors: Nathan Foran, Daniel Carpintero, Oluwalayomi Giwa

Helper functions for the Student Record Program.

This file contains all reusable functions that handle input validation and dictionary
operations such as adding a student, searching for a record, editing a name, and
removing a student. These functions support the main program by keeping the logic
organized and reducing repeated code.

Inputs: raw user input (integers, floats, text), student ID keys.
Processing: validation checks, type conversions, dictionary lookups/updates.
Outputs: cleaned values, student records, and True/False results.
"""

# Input Validation
def input_int(prompt, accept_neg1=False):
    """
    Ask the user for an integer. Keeps asking until a valid integer is entered.
    If accept_neg1 is True, the value -1 is allowed (used for cancel menus).
    """
    while True:
        value = input(prompt)
        if value.lstrip("-").isdigit():
            num = int(value)
            if num == -1 and not accept_neg1:
                print("Negative one is not allowed here.")
            else:
                return num
        else:
            print("Invalid integer. Try again.")


def input_float(prompt, min_val, max_val):
    """
    Ask the user for a floating-point number within a given range.
    Continues asking until a valid value is entered.
    """
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid float. Try again.")


def input_nonempty(prompt):
    """
    Ask the user for a non-empty string.
    Used for names and other text inputs.
    """
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input cannot be empty.")


# Student Operations
def search(students, student_id):
    """
    Look up a student ID in the dictionary.
    Returns the student record if found, otherwise None.
    """
    return students.get(student_id)


def add(students, student_id, name, gpa, semester):
    """
    Add a student to the dictionary using their ID as the key.
    Overwrites if the ID already exists.
    """
    students[student_id] = {"name": name, "gpa": gpa, "semester": semester}


def edit_name(students, student_id, new_name):
    """
    Change the name of a student if they exist.
    """
    if student_id in students:
        students[student_id]["name"] = new_name


def remove(students, student_id):
    """
    Remove a student by ID.
    Returns True if the student was removed, otherwise False.
    """
    return students.pop(student_id, None) is not None
