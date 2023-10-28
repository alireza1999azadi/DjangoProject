from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('hi user.. im hello world!')
    return render(request , 'about.html')
def home(request):
    # return HttpResponse('This here home!')
    return render(request, 'home.html')