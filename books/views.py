from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def book_detail(request, id):
    return HttpResponse("Book {}".format(id))
