from urllib import request
from django.shortcuts import render, HttpResponse

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
     return render (request, 'contact.html')
