from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")
    # else: 
    return render(request, 'index.html')
    # messages.success(request, "This is a test message")
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email' )
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact= Contact(name=name ,email= email,phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
# def logoutUser(request):
#     logout(request)
#     return redirect("/login")


# def loginUser(request):
#     # return render(request, 'login.html')
#     if request.method== "POST":
#         username= request.POST.get('username')
#         password= request.POST.get('password')
#         print(username, password)
#         user= authenticate(username=username, password= password)
        

#         # user = authenticate(username='john', password='secret')
#         if user is not None:
#             login(request, user)
#              # A backend authenticated the credentials
#             return redirect("/")
#             # return render(request, 'index.html')
#         else:
#             return render(request, 'login.html')
     
    # return render(request, 'login.html')
def ex(request):
    return render(request, 'ex.html')
def pnp(request):
    return render(request, 'pnp.html')

def crs(request):
    return render(request, 'crs.html')