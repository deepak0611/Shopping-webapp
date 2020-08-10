from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>This is just starting page.go to shop by typing /shop/ in url .</h2>")