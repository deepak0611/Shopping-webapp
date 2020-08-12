from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return  render(request,'index.html')
    # return HttpResponse("<h2>This is just starting page.go to shop by typing /shop/ in url .</h2>")