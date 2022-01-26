from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# class UserData(forms.Form):
  


def index(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse("login"))
  else:
    return render(request,'users/user.html',{
      "request":request
    })

def register(request):
  if request.user.is_authenticated:
    return render(request,'users/user.html',{
      "request":request
    })

  else:
    if request.method=="POST":
      form=UserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("login"))
    else:
      form=UserCreationForm()
    return render(request,'users/register.html',{
      "form":form
    })

  

def login_view(request):
  if request.user.is_authenticated:
    return render(request,'users/user.html',{
      "request":request
    })
  else:
    if request.method=="POST":
      username=request.POST["username"]
      password=request.POST["password"]

      user=authenticate(request,username=username,password=password)
      if user is not None:
        login(request,user)
        return render(request,'users/user.html',{
          "request":request
        })
      else:
        return render(request,'users/login.html',{
          "message":"Invalid crendtials."
        })
    return render(request,'users/login.html')

def logout_view(request):
  logout(request)
  return render(request,'users/login.html',{
    "message":"Logged out"
  })






  
