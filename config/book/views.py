from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("Book")


def about(request):
    return HttpResponse("about")


def pageNotFound(request, exception):
    return HttpResponseNotFound("Not Found")
