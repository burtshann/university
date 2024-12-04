from django.db import models

# Create your models here.
from django.db import models

from management.utils import convert_to_gpa


class Student(models.Model):
    student_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    major = models.CharField(max_length=100)
    enrollment_year = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return self.name

class Instructor(models.Model):
    instructor_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
# management/models.py
from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    major = models.CharField(max_length=100)
    enrollment_year = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    grade = models.FloatField()  # 成绩以百分制表示

    def get_gpa(self):
        return convert_to_gpa(self.grade)

    def __str__(self):
        return f"{self.student.name} - {self.course.name} ({self.semester})"
