from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post(request):
    return HttpResponse('This is post page')
def detail(request):
    return HttpResponse("This is detail of previous article")
def comments(request):
    return HttpResponse("This is comments of out post")