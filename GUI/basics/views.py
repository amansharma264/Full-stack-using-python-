from django.shortcuts import render
from django.conf import settings
from .models import StudentDepartment  # Make sure this exists

def abc(request):
    return render(request, "abc.html")

def led(request):
    return render(request, "led.html")

def counter(request):
    result = 0
    if request.method == "POST":
        data = request.POST
        result = data.get('result')
        if not result:
            result = 0
        else:
            result = int(result)
        if 'Increament' in request.POST:
            result += 1
        elif 'Decreament' in request.POST:
            result -= 1
        elif 'Reset' in request.POST:
            result = 0
        return render(request, "counter.html", {'result': result})
    return render(request, "counter.html", {'result': result})

def calci(request):
    if(request.method=="POST"):
        data=request.POST
        firstnumber=int(data.get('textfirstnumber'))
        secondnumber=int(data.get('textsecondnumber'))
        if('buttonadd' in request.POST):
            result=firstnumber+secondnumber
            return render(request,'calci.html',context={'result': "sum="+str(result)})
        if('buttonsub' in request.POST):
            result=firstnumber-secondnumber
            return render(request,'calci.html',context={'result': "sub="+str(result)})
        if('buttonmul' in request.POST):
            result=firstnumber*secondnumber
            return render(request,'calci.html',context={'result': "mul="+str(result)})
        if('buttondiv' in request.POST):
            if secondnumber != 0:
                result=firstnumber/secondnumber
                return render(request,'calci.html',context={'result': "div="+str(result)})
            else:
                return render(request,'calci.html',context={'result': "Cannot divide by 0"})
    return render(request,'calci.html')

def department(request):
    if(request.method=="POST"):
        data = request.POST
        deptname = data.get('textdepartmentname')
        deptdesc = data.get('textdepartmentdesc')
        StudentDepartment.objects.create(DEPT_NAME=deptname, DEPT_DESC=deptdesc)
        result = "Department Details saved successfully"
        return render(request, 'department.html', context={'result': result})
    return render(request, 'department.html')

def departmentview(request):
    getdepartment = StudentDepartment.objects.all()
    return render(request, "departmentview.html", context={'getdepartment': getdepartment})
