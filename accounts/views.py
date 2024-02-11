from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate,login,logout
# Create your views here.

def register_user(request):
    if request.method=="POST":

        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('user_name')
        password=request.POST.get('password')
        con_password=request.POST.get('con_password')

        user=User.objects.filter(username=username)
        if user.exists():
            return render(request,'./account/register.html',{'message':'Username already use'})

        if  password==con_password:
            user=User.objects.create(first_name=first_name,last_name=last_name,username=username)
            user.set_password(password)
            user.save()
            return redirect('login')
        
        else:
            return render(request,'./account/register.html',{'message':'Confirm Password is not matched'})
        
    return render(request,'./account/register.html',{})

def login_page(request):
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        print(username,password)

        user=User.objects.filter(username=username)

        if not user.exists():
            return render(request,'./account/login.html',{'message':'Invalid Username'})
        
        user=authenticate(username=username , password=password)
        if user is None:
            return render(request,'./account/login.html',{'message':'Invalid Password'})
        else:
            login(request,user)
            return redirect('/home')
        
    return render(request,'./account/login.html',{'message':'Login'})


def logout_page(request):
    logout(request)
    return redirect('/home')