from django.urls import path
from . import views
# from django.contrib.auth.views import LogoutView
# from django.contrib.auth.views import LogoutView
# from django.contrib.auth import views as auth_views
# from .views import LoginPage

urlpatterns = [
    path('',views.home, name = 'home'),
    path('home',views.home, name = 'home'),
    path('sign-up',views.sign_up, name = 'sign_up'),
    path('create-post',views.create_post, name = 'create_post'),
    
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]
