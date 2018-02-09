from django.shortcuts import render, render_to_response
from django.http import HttpResponse


def index(request):
    return HttpResponse("main page")

def error404(request):
    return render(request, 'webapp/404.html')


def error500(request):
    return render(request, 'webapp/404.html')
