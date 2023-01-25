
from django.urls import path
from .views import about, ArticlesHome, ShowPost, AddPage,\
    RegisterUser, logout_user, LoginUser, ContactFormView

urlpatterns = [
    path('', ArticlesHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),

]
