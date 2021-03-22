from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import application
from .models import tarifa
from datetime import date 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ApplicationForm
from django.forms import ModelForm

# Create your views here.
@login_required
def ApplicationsListToday(request):  
    applications_today = application.objects.filter(fecharegistro=date.today())  
    return render(request,'registration/applications_list_today.html',{'applications_today':applications_today}) 

def ApplicationsCreate(request): 
    #applications_hoy = application.objects.filter(fecharegistro=date.today())
    if request.method == "POST": 
        form = ApplicationForm(request.POST or None)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.usuario = User.objects.get(pk=request.user.id)
            newform.estado= "R"
            newform.save()
            model = form.instance
            return redirect('/register')  
    else:
        form = ApplicationForm()   
    return render(request,'registration/applications_create.html',{'form':form})    

def ApplicationsUpdate(request, id):  
    applicationtoedit = application.objects.get(id=id)
    form = ApplicationForm(initial={'fecharegistro':applicationtoedit.fecharegistro,
                                    'ficharegistral': applicationtoedit.ficharegistral, 
                                    'dni': applicationtoedit.dni, 
                                    'nombres': applicationtoedit.nombres, 
                                    'tarifa': applicationtoedit.tarifa,
                                    'doc_adjuntos':applicationtoedit.docs_adjuntos,
                                    'observaciones':applicationtoedit.observaciones})
    if request.method == "POST":  
        form = ApplicationForm(request.POST, instance=applicationtoedit)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/register')  
            except Exception as e: 
                pass    
    return render(request,'registration/applications_update.html',{'form':form})  

def ApplicationsDelete(request, id):
    applicationtodelete = application.objects.get(id=id)
    try:
        applicationtodelete.delete()
        return redirect('/register') 
    except:
        pass
    