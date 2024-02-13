from django.shortcuts import render
from django.http import HttpResponse

def ban(request):
    return HttpResponse('we know who we know')
