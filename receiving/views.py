from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from register.models import application


# Create your views here.
@login_required

def applications_estado_r(request):  # All applications with "R"
    applications = application.objects.filter(estado="R")  
    return render(request,'registration/applications_estado_r.html',{'applications':applications})  
    
def applications_estado_o(request):  # All applications with "O"
    applications = application.objects.filter(estado="O")  
    return render(request,'registration/applications_estado_o.html',{'applications':applications})

def handin(request):
    context = { 'message': "Hand In DNIs" } 
    return render(request, 'registration/handin.html', context) 