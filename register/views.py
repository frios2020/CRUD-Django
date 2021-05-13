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
def isvalid_query_param(param):
    return param != '' and param is not None

def ApplicationsListToday1(request): 
    qs = application.objects.all()
    fi = request.GET.get('FI')
    ff = request.GET.get('FF')
    DNI = request.GET.get('DNI')
    FR = request.GET.get('FichaRegistral')
    Nombres = request.GET.get('Nombres')
    if fi!='' and fi is not None:
        qs = qs.filter(fecharegistro__gte = fi)
    if ff!='' and ff is not None:
        qs = qs.filter(fecharegistro__lte = ff)
    if FR!='' and FR is not None:
        qs = qs.filter(ficharegistral__icontains = FR)
    if Nombres!='' and Nombres is not None:
        qs = qs.filter(nombres__icontains = Nombres)
    context = {
            'queryset': qs

    }
    return render(request,'registration/applications.html',context) 

def ApplicationsListToday(request):  
    applications_today = application.objects.filter(fecharegistro=date.today())  
    return render(request,'registration/applications_list_today.html',{'applications_today':applications_today}) 

def ApplicationsFilterbyDate(request, fi, ff):
    applications_given_date = application.objects.filter(fecharegistro >= fi and fecharegistro <= ff)
    return render(request, 'registration/applications_list_today.html',{'applications_given_date':applications_given_date})

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
    