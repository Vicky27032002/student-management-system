from django import forms
from .models import Department, Student

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name' , 'email' , 'phone' , 'department']        