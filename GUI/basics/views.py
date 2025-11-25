from django.shortcuts import render
from django.conf import settings

def abc(request):
    return render(request, "abc.html")

def led(request):
    return render(request, "led.html")

def counter(request):
    result = 0  # Default value

    if request.method == "POST":
        data = request.POST
        result = data.get('result')

        # If result is empty or None → default to 0
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

    # On GET request, send initial data
    return render(request, "counter.html", {'result': result})

def calci(request):
    if(request.method=="POST"):
        data=request.POST
        firstnumber=int(data.get('textfirstnumber'))
        secondnumber=int(data.get('textsecondnumber'))
        if('buttonadd' in request.POST):
            result=firstnumber+secondnumber
            return render(request,'calci.html',context={'result': "sum="+str{result}})
        if('buttonadd' in request.POST):
            result=firstnumber-secondnumber
            return render(request,'calci.html',context={'result': "sub="+str{result}})
        if('buttonadd' in request.POST):
            result=firstnumber*secondnumber
            return render(request,'calci.html',context={'result': "mul="+str{result}})
        if('buttonadd' in request.POST):
            result=firstnumber/secondnumber
            return render(request,'calci.html',context={'result': "div="+str{result}})
        
    return render(request,'calci.html')
