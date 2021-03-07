from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import User
from .forms import EmployeeForm
# Create your views here.
def home(request):
    return render(request, 'core/home.html')
#Attendence
def attend(request):
    return render(request, 'core/attendance.html')
#addEmp
def addemp(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = User.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'core/addEmp.html', {'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = User.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/dash')
#dashboard
def dash(request):
    context = {'dash': User.objects.all()}
    return render(request, 'core/dashboard.html',context)

def employee_delete(request,id):
    if request.method == 'POST':
        employee = User.objects.get(pk=id)
        employee.delete()
        return HttpResponseRedirect('/dash')

def employee_update(request, id):
    return redirect('')

#logout
def User_logout(request):
     return HttpResponseRedirect('/')