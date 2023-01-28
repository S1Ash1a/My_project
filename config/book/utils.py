
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить пост", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]


class DataMixin:

    def get_user_context(self, **kwargs):  #формирует нужный контекст#
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated: #проверка на авторизацию и кто видет таблицу по добавлению#
            user_menu.pop(1)
        context['menu'] = user_menu
        if 'cat_selected' not in context:   #проверка ключа#
            context['cat_selected'] = 0
        return context
