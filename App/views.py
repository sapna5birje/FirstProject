from django.shortcuts import render, redirect, reverse

# Create your views here.
#from django.shortcuts import render
from django.http import HttpResponse
from App.models import *

def index(request):
    '''checking branch'''

    employee=Employees.objects.all()
    for n in employee:
        print(n.FirstName,n.Address,n.EmailAddress)

    context={
    'employeedata':employee
    }
    return render(request, 'templates.html', context)

"""def Add(request):
    
    firstname=request.POST.get('FirstName')
    lastname=request.POST.get('LastName')
    Address=request.POST.get('Address')
    emailaddress=request.POST.get('EmailAddress')
    date=request.POST.get('Date')
    employeeinsert=Employees(FirstName=firstname,Address=Address,LastName=lastname,EmailAddress=emailaddress,Date=date)
    employeeinsert.save()

    employee=Employees.objects.all()
    for n in employee:
        print(n.FirstName,n.Address,n.EmailAddress)

    context={
    'employeedata':employee
    }
    return render(request, 'templates.html', context)"""
def Add(request):
    if request.POST.get("submit"):
        firstname=request.POST.get('FirstName')
        lastname=request.POST.get('LastName')
        Address=request.POST.get('Address')
        emailaddress=request.POST.get('EmailAddress')
        date=request.POST.get('Date')
        print(firstname)
        employeeinsert=Employees(FirstName=firstname,Address=Address,LastName=lastname,EmailAddress=emailaddress,Date=date)
        employeeinsert.save()

       
        return redirect(reverse('index', kwargs={}))
    else:

        return render(request, 'Add.html')
        #return redirect(reverse('index', kwargs={}))

def update(request, id):
    employee=Employees.objects.filter(id=id).last()
    context={
    'employeedata':employee,
    }
    

    return render(request,'Update.html',context)

def updaterecord(request,id):
    firstname=request.POST.get('FirstName')
    lastname=request.POST.get('LastName')
    Address=request.POST.get('Address')
    emailaddress=request.POST.get('EmailAddress')
    date=request.POST.get('Date')

    employee=Employees.objects.get(id=id)
    employee.FirstName=firstname
    employee.LastName=lastname
    employee.EmailAddress=emailaddress
    employee.Date=date
    employee.Address=Address
    employee.save()
    employee=Employees.objects.all()

    context={
    'employeedata':employee
    }

    return render(request,'templates.html',context)








def Delete(request):
    itemid=request.POST['ID']
    print(itemid)
    employee=Employees.objects.filter(id=itemid)
    employee.delete()
    employee=Employees.objects.all()

    context={
    'employeedata':employee
    }
    return render(request, 'templates.html', context)






    
    