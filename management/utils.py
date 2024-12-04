# management/utils.py
def convert_to_gpa(grade):
    if grade >= 90:
        return 4.0
    elif grade >= 85:
        return 3.7
    elif grade >= 80:
        return 3.3
    elif grade >= 75:
        return 3.0
    elif grade >= 70:
        return 2.7
    elif grade >= 65:
        return 2.3
    elif grade >= 60:
        return 2.0
    elif grade >= 50:
        return 1.0
    else:
        return 0.0
