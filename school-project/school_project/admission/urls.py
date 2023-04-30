from django.urls import path
from admission . views import addadmission
from admission . views import admissionreport

urlpatterns = [
   
    path('newadm/',addadmission),
    path('admreport/',admissionreport),
    
]