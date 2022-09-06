from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail

from .models import Contacts

# Create your views here.
def home(request):
    if request.method=='POST':
        
        email=request.POST.get('email')
        usn=request.POST.get('usn')
        name=request.POST.get('name')
        contact=Contacts(name=name,usn=usn,email=email)
        if name and usn and email:
            contact.save()
            send_mail(
    'Evening mail',
    'Mail by Django ',
    'yashaswisingh47@gmail.com',
    [email],
    fail_silently=False,
)
            return redirect('page')
        else:
            return HttpResponse("Enter all details")
        
    return render(request,'index.html')



def page(request):
    return render(request,'page.html')