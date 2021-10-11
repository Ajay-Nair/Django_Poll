from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request , question_id):
    return HttpResponse("You are looking at question %s."%question_id)

def results(request , question_id):
    response = ("The results of question %s")
    return(response % question_id)

def vote(request , question_id):
    return HttpResponse("Your voting on question %s."%question_id)
