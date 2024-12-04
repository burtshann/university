from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Course, Instructor, Enrollment

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Enrollment)



