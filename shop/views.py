from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    # pdt=Product.objects.all()
    # rangerr=range(0,2)
    cats=Product.objects.values('category').distinct()
    # print(cats)
    pdt=[]
    for cat in cats:
        prod=Product.objects.filter(category=cat['category'])
        pdt.append(prod)


    return render(request,'shop/index.html',{'product':pdt})

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    msg=""
    flag=False
    data=0
    if(request.method=='POST'):
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        data=contact
        contact.save()
        msg="Your response has been taken."
        flag=True


    return render(request, 'shop/contact.html',{'msg':msg,'flag':flag,'data':data})


def tracker(request):
    return render(request,'shop/tracker.html')

def add_item(request):
    return render(request,'shop/add_item.html')

def search(request):
    return  HttpResponse("This is search")


def prodView(request):
    return  HttpResponse("This is prodView")

def checkout(request):
    return  HttpResponse("This is checkout")