from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Articles

menu = [{'title': "Обо мне", 'url_name': 'about'},
        {'title': "Добавить пост", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = Articles.objects.all()
    data = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'book/index.html', data)


def about(request):
    return render(request, 'book/about.html', {'title': 'Обо мне', 'menu': menu})


def addpage(request):
    return HttpResponse("Форма по добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound("Not Found")


def show_post(request, post_slug):
    post = get_object_or_404(Articles, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post,
    }

    return render(request, 'book/post.html', context=context)
