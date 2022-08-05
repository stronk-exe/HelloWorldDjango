from django.shortcuts import render
from django.http import HttpResponse

def sayHi(request):
    return render(request, 'hello.html', {'name':'stronk'})
