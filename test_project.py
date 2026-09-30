import pytest
from project import calculate_grade, calculate_average, class_statistics

def test_calculate_grade():
    student = {
        "python": 85,
        "maths": 90,
        "C++": 88
    }
    assert calculate_grade(student) == "B"

def test_calculate_grade_A():
    student = {
        "python": 95,
        "maths": 92,
        "C++": 96
    }
    assert calculate_grade(student) == "A"

def test_calculate_grade_F():
    student = {
        "python": 35,
        "maths": 42,
        "C++": 38
    }
    assert calculate_grade(student) == "F"

def test_calculate_average():
    student = {
        "name": "Arun",
        "python": 95,
        "maths": 90,
        "C++": 78
    }
    assert calculate_average(student) == pytest.approx(87.6666666667)

def test_class_statistics():
    students = [
        {
            "id": 101,
            "name": "Arun",
            "department": "ECE",
            "year": 2,
            "python": 95,
            "C++": 90,
            "maths": 85
        },
        {
            "id": 102,
            "name": "Karthik",
            "department": "CSE",
            "year": 2,
            "python": 70,
            "C++": 75,
            "maths": 80
        },
        {
            "id": 103,
            "name": "Ravi",
            "department": "ECE",
            "year": 2,
            "python": 90,
            "C++": 95,
            "maths": 100
        }
    ]
    avg, highest, lowest, grades = class_statistics(students)

    assert avg == pytest.approx(86.6666666667)
    assert highest["name"] == "Ravi"
    assert lowest["name"] == "Karthik"
    assert grades["A"] == 2
    assert grades["B"] == 0
    assert grades["C"] == 1

def test_calculate_grade_boundary_A():
    student = {
        "python": 90,
        "maths": 90,
        "C++": 90
    }
    assert calculate_grade(student) == "A"

def test_calculate_grade_boundary_B():
    student = {
        "python": 80,
        "maths": 80,
        "C++": 80
    }
    assert calculate_grade(student) == "B"

def test_class_statistics_empty():
    students = []
    assert class_statistics(students) is None
