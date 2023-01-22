from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Articles

menu = ["Обо мне", "Добавить пост", "Обратная связь", "Войти"]


def index(request):
    posts = Articles.objects.all()
    return render(request, 'book/index.html', {'posts': posts, 'menu': menu})


def about(request):
    return render(request, 'book/about.html', {'title': 'Обо мне'})


def pageNotFound(request, exception):
    return HttpResponseNotFound("Not Found")
