from django.shortcuts import render


# Create your views here.

def feecollection(request):
    return render(request,'finance/feecollection.html')

def feeduesreport(request):
    return render(request,'finance/feeduesreport.html')


def feecollectionreport(request):
    
    return render(request,'finance/collectionreport.html')      
    
       

