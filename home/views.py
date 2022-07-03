from unicodedata import name
from urllib import request
from django.shortcuts import render, HttpResponse

from home.models import Contact
from datetime import datetime

# Create your views here.

def index (request):
    context={
        'variable':"Joel DJ is great",
        'variable1':"Jaison MahaBuddhi"
        }
    return render (request, 'index.html')
    # return HttpResponse("this is home page")
def about (request):
    return render (request, 'about.html')
    
def services (request):
     return render (request, 'services.html')

    
def contact (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date = datetime.today() )
        contact.save()
    return render (request, 'contact.html')
