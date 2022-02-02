
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import myuser1
from django.contrib.auth import login,authenticate
# Create your views here.
def home(request):
   return render(request,'pages/home.html')

def contact(request):
 return render(request,'pages/contact.html')
 
def about(request):
 return render(request,'pages/about.html')

def login(request):
    context={};
    
    if(request.method=='POST') :
        name=request.GET['uname1']
        password=request.GET['psw1']
        try:
            user=myuser1.em
    else:
     print(request.GET)
     
     myuser11=myuser1();
     if( myuser11.name==name and myuser11.password==password):
        return render(request,'pages/home.html') 

def register(request):
    context={};
    context['id']=1
    if(request.method=='POST') :
       name=request.POST.get['uname']
       password=request.POST.get['psw']
       return render(request,'pages/register.html',context)
    else:
     print(request.POST)
     name=request.POST['uname']
     password=request.POST['psw']
     myuser11=myuser1()
     myuser11.name=name
     myuser11.password=password
     myuser11.save()


     context['message']='user inserted'
     return render(request,'pages/register.html',context)    
