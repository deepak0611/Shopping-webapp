from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from datetime import date
from .models import *

# Create your views here.
def index(request):
    # pdt=Product.objects.all()
    # rangerr=range(0,2)
    pdt=Product.objects.all()



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
    if request.method == 'POST' and request.FILES['myimage']:
        name=request.POST.get('name','')
        category=request.POST.get('category','')
        price=request.POST.get('price','')
        desc=request.POST.get('desc','')
        myimage=request.FILES['myimage']
        product=Product(product_name=name,category=category,price=price,desc=desc,image=myimage,pub_date=date.today())
        product.save()
    return render(request,'shop/add_item.html')

def search(request):
    return  HttpResponse("This is search")


def prodView(request):
    return  HttpResponse("This is prodView")

def checkout(request):
    if request.method == "GET":
        # return render(request, 'shop/hihi.txt')
        return  HttpResponse("This is checkout")

    return  HttpResponse("This is error")