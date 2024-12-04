from django import forms
from .models import Student, Course, Instructor, Enrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'birth_date', 'major', 'enrollment_year']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id', 'name', 'instructor', 'credits']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['instructor_id', 'name', 'department', 'email']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'semester', 'grade']
