from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import Employee
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html',{})

#Retrieve  list   of all employees.
@login_required(login_url='login')
def view_all_enployee(request):
    employees=Employee.objects.all()
    print(employees)
    context={
        'employees': employees
    }
    return render(request,'view_all_employee.html',context=context)

@login_required(login_url='login')
def add_employee(request):
    if request.method=='POST':
        name=request.POST['name']
        position=request.POST['position']
        department=request.POST['department']
        
    
        new_emp=Employee.objects.create(name=name,position=position,department=department)
        return redirect('/view_emp')
    return render(request,'Add_employees.html')

@login_required(login_url='login')
def remove_employee(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return redirect('/view_emp')
        except:
            return HttpResponse("<h1>please enter valid Emp id</h1>")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_employee.html',context=context)


@login_required(login_url='login')
def filter_employee(request):
    if request.method=='POST':
        id=int(request.POST['id'])
      

        emps=Employee.objects.all()
        if id:
            emps=emps.filter(id__icontains=id)

        context={
            'employees':emps
        }

        return render(request,'view_all_employee.html',context=context)
    return render(request,'filter_employee.html')

@login_required(login_url='login')
def update_details(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        position=request.POST['position']
        department=request.POST['department']

        employee.name=name
        employee.position=position
        employee.department=department
        employee.save()
        return redirect('/view_emp')


    context={'employee':employee}
    return render(request,'update_details.html',context=context)