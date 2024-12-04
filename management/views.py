from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Course, Instructor, Enrollment
from .forms import StudentForm, CourseForm, InstructorForm, EnrollmentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'management/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'management/student_detail.html', {'student': student})

def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'management/student_edit.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'management/student_edit.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')

# 类似的视图可以为课程和讲师创建
def gpa_report(request):
    # 示例代码：计算每个学期的平均GPA
    enrollments = Enrollment.objects.all()
    gpa_data = {}
    for enrollment in enrollments:
        semester = enrollment.semester
        grade = enrollment.grade
        if semester not in gpa_data:
            gpa_data[semester] = {'total_grade_points': 0, 'total_credits': 0}
        gpa_data[semester]['total_grade_points'] += grade_to_points(grade) * enrollment.course.credits
        gpa_data[semester]['total_credits'] += enrollment.course.credits
    for semester in gpa_data:
        gpa_data[semester]['average_gpa'] = gpa_data[semester]['total_grade_points'] / gpa_data[semester]['total_credits']
    return render(request, 'management/gpa_report.html', {'gpa_data': gpa_data})

def grade_to_points(grade):
    # 示例代码：将成绩转换为GPA分数
    grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    return grade_points.get(grade, 0.0)

# 新增主页视图
def home(request):
    return render(request, 'management/home.html')

# 其他视图
def student_list(request):
    students = Student.objects.all()
    return render(request, 'management/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'management/student_detail.html', {'student': student})

def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'management/student_edit.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'management/student_edit.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')

# def average_gpa(request, semester):
#     enrollments = Enrollment.objects.filter(semester=semester)
#     total_gpa = sum([convert_to_gpa(e.grade) for e in enrollments])
#     average_gpa = total_gpa / len(enrollments)
#     return render(request, 'management/average_gpa.html', {'average_gpa': average_gpa})

# def at_risk_students(request):
#     students = Student.objects.filter(enrollment__grade__lte='C')
#     return render(request, 'management/at_risk_students.html', {'students': students})
# management/views.py
from django.shortcuts import render
from .models import Enrollment


def semester_avg_gpa(request):
    enrollments = Enrollment.objects.all()
    semesters = enrollments.values_list('semester', flat=True).distinct()

    avg_gpa_per_semester = {}

    for semester in semesters:
        semester_enrollments = enrollments.filter(semester=semester)
        total_gpa = sum([enrollment.get_gpa() for enrollment in semester_enrollments])
        avg_gpa = total_gpa / len(semester_enrollments)
        avg_gpa_per_semester[semester] = avg_gpa

    return render(request, 'management/semester_avg_gpa.html', {'avg_gpa_per_semester': avg_gpa_per_semester})


def identify_at_risk_students(request, threshold=2.0):
    enrollments = Enrollment.objects.all()
    at_risk_students = {}

    for enrollment in enrollments:
        if enrollment.get_gpa() < threshold:
            if enrollment.student not in at_risk_students:
                at_risk_students[enrollment.student] = []
            at_risk_students[enrollment.student].append(enrollment)

    return render(request, 'management/at_risk_students.html', {'at_risk_students': at_risk_students})
