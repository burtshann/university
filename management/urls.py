from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/new/', views.student_new, name='student_new'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    # 添加其他URL模式
    path('semester_avg_gpa/', views.semester_avg_gpa, name='semester_avg_gpa'),
    path('at_risk_students/', views.identify_at_risk_students, name='at_risk_students'),

]
