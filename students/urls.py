from django.urls import path
from .views import *

urlpatterns = [
    # Departmwnt URLs
    path('departments/', department_list, name = 'department_list'),
    path('departments/add/', department_create, name = 'department_create'),
    path('departments/edit/<int:id>/', department_update, name = 'department_update'),
    path('departments/delete/<int:id>/', department_delete, name = 'department_delete'),

    # Student URLs
    path('students/', student_list, name = 'student_list'),
    path('students/add/', student_create, name = 'student_create'),
    path('students/edit/<int:id>/', student_update, name = 'student_update'),
    path('students/delete/<int:id>/', student_delete, name = 'student_delete'),
]