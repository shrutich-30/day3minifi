def calculate_grade(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100")

    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def student_result(name, marks):
    return {
        "name": name,
        "marks": marks,
        "grade": calculate_grade(marks),
    }
