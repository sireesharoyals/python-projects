from django.shortcuts import render
from admission.models import student


# Create your views here.

def homepage(request):
    return render(request,'index.html')


def addadmission(request):
     return render( request,'admission/addadmission.html')

def admissionreport(request):
    result=student.objects.all()
    students={"allstudents":result}
   
    return render(request,'admission/admissionreport.html',students) 


