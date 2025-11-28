# Student Record Program – Assignment 2
CPRG 216 – Assignment 2

**Authors:** Nathan Foran, Daniel Carpintero, Oluwalayomi Giwa

This repository contains a menu-driven Python application for managing student records. The program allows the user to add, search, edit, and remove students, with all data stored in a dictionary using the student ID as the key.

---

## Features

* Add a new student (ID, name, GPA, semester)
* Search for a student by ID
* Edit a student's name
* Remove a student from the record
* Input validation for IDs, GPA values, and empty text
* Menu-based navigation with options to continue or exit

---

## Repository Structure

```
assignment2.py            # Main program and menu handling
functions.py              # Helper functions for input and student operations
Output.txt                # Required assignment test run output
a2_PDL.txt                # Program Design Language description
a2_flowchart.png          # Simple flowchart
a2_flowchart_complex.png  # Detailed flowchart
README.md                 # This file
```

---

## How to Run

1. Ensure all `.py` files are in the same folder.
2. Run the main file:

```
python assignment2.py
```

3. Follow the prompts shown in the terminal.

---

## Program Overview

The system stores students in a dictionary structure like this:

```python
students = {
    123: {
        "name": "Example Name",
        "gpa": 3.1,
        "semester": 3
    }
}
```

The main program (`assignment2.py`) displays the menu and calls the appropriate functions in `functions.py` based on user input.

---

## Documentation Included

* **test_output.txt** – Sample run demonstrating required assignment behavior
* **PDL.txt** – Step-by-step program logic in PDL format
* **a2_flowchart.png** – Basic flowchart of the program
* **a2_flowchart_complex.png** – Full, detailed flowchart version

---

## Notes

* No external libraries are required.
* The program uses simple Python features appropriate for academic assignment use.
* Files are structured to keep the logic clear and maintainable.
