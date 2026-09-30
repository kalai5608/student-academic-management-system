# Student Academic Management System

## Video Demo

[YouTube Video](https://youtu.be/01mDu9bi9cE)

## Description

The Student Academic Management System is a command-line Python application designed to manage student academic records. I created this project as my final project for CS50's Introduction to Programming with Python (CS50P). The main purpose of the project is to bring together several Python concepts that I learned throughout the course and use them to create a practical application.

The program stores information about students, including their student ID, name, department, year of study, and marks in Python, C++, and Maths. Users can interact with the application through a menu displayed in the terminal.

## Features

The application provides several options for managing student records. Users can add new students, view all existing students, search for a particular student using their ID, update student information, and delete student records. The program checks user input before accepting it. For example, student IDs must be valid and unique, the year of study must be within the appropriate range, and marks must be between 0 and 100.

The program can also perform academic calculations. The average mark of an individual student can be calculated, and a grade is assigned based on the student's average. The class statistics feature processes all students and calculates the overall class average. It also identifies the students with the highest and lowest averages and displays the distribution of grades in the class.

## File Handling

One of the important features of the project is persistent data storage. Student records are saved in a CSV file named `students.csv`. The `save_students` function writes the records to the file, while the `load_students` function reads the records when the program starts. This means that the student information does not disappear when the program is closed.

I used Python's built-in `csv` module for this functionality. This also gave me an opportunity to practice reading from and writing to files, handling CSV headers, and converting stored values back into the appropriate data types.

## Files

### `project.py`

This is the main program file. It contains the `main` function and the functions used for adding, viewing, searching, updating, deleting, calculating grades and averages, generating statistics, and handling CSV files.

### `test_project.py`

This file contains automated tests written using `pytest`. The tests cover grade calculation, average calculation, class statistics, grade boundaries, and the case where there are no students. There are currently eight passing tests.

### `students.csv`

This CSV file stores the student records so that they can be loaded again when the program is restarted.

## Technologies Used

* Python
* CSV file handling
* pytest

## How to Run

Make sure Python is installed, open the project folder in a terminal, and run:

```bash
python project.py
```

To run the automated tests:

```bash
pytest
```

## Project Purpose

This project helped me practice and combine Python functions, lists, dictionaries, loops, conditional statements, input validation, file I/O, and automated testing in one complete application. It also helped me understand how individual functions can be combined to create a larger, organized program.
