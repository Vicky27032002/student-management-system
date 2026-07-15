from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Student
from .forms import DepartmentForm, StudentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Department Views

@login_required
def department_list(request):
    departments = Department.objects.all()
    context = {
        'departments' : departments
    }
    return render(request, 'students/department_list.html', context)

@login_required
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

@login_required
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

@login_required
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

@login_required
def student_list(request):
    students = Student.objects.all()
    context = {
        "students" : students
    }
    return render(request, 'students/student_list.html', context)

@login_required
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

@login_required
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

@login_required
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    context = {
        "student" : student
    }   
    return render(request, 'students/student_confirm_delete.html', context)  

@login_required
def dashboard(request):
    total_departments = Department.objects.count()
    total_students = Student.objects.count()
    context = {
        "total_departments" : total_departments,
        "total_students" : total_students
    }
    return render(request, 'students/dashboard.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username = username,
            password = password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'students/login.html')      

def user_logout(request):
    logout(request)
    return redirect('login')  