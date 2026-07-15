from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Student
from .forms import DepartmentForm, StudentForm

# Department Views

def department_list(request):
    departments = Department.objects.all()
    context = {
        'departments' : departments
    }
    return render(request, 'students/department_list.html', context)

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    context = {
        "form" : form
    }    
    return render(request, 'students/department_form.html', context)

def department_update(request, id):
    department = Department.objects.get(id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    context = {
        "form" : form
    }        
    return render(request, 'students/department_form.html', context)

def department_delete(request, id):
    department = get_object_or_404(Department, id=id)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    context = {
        "department" : department
    }
    return render(request, 'students/department_confirm_delete.html', context)


# Student Views

def student_list(request):
    students = Student.objects.all()
    context = {
        "students" : students
    }
    return render(request, 'students/student_list.html', context)

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    context = {
        "form" : form
    }     
    return render(request, 'students/student_form.html', context)  

def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    context = {
        "form" : form
    }   
    return render(request, 'students/student_form.html', context)

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    context = {
        "student" : student
    }   
    return render(request, 'students/student_confirm_delete.html', context)  
