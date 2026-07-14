from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from .forms import DepartmentForm

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