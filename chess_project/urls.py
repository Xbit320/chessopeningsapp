"""chess_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from openings import views
from users import views as user_views
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', views.opening_bar,name="index"),
    path('detail/<int:id>', views.detail,name='detail'),
    path('detail/puzzle/<int:id>', views.opening_puzzle,name='opening_puzzle'),
    path('register/', user_views.register, name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout',),
    path('profile/', user_views.profilepage,name='profile'),
    path('profile/opening/delete/<int:id_opening>', user_views.delete_follow, name='delete'),
    path('profile/opening/add/<int:id_opening>', user_views.add_follow, name='add'),

    path('password_change/done/', authentication_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', authentication_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', authentication_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', authentication_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', authentication_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', authentication_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),

]
