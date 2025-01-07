from django.shortcuts import render
from django.http import HttpRequest
def home(request):
    return render(request,'ellora_app/index.html')
