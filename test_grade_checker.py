import pytest

from grade_checker import calculate_grade, student_result


def test_grade_a():
    assert calculate_grade(95) == "A"


def test_grade_b():
    assert calculate_grade(80) == "B"


def test_grade_c():
    assert calculate_grade(65) == "C"


def test_grade_d():
    assert calculate_grade(45) == "D"


def test_fail_grade():
    assert calculate_grade(30) == "F"


def test_invalid_marks():
    with pytest.raises(ValueError):
        calculate_grade(120)


def test_student_result():
    result = student_result("Student", 92)

    assert result["grade"] == "A"
