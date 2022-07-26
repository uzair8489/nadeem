from re import template
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('blogs', views.blogs, name='blogs'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('services', views.services, name='services'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('change_password', auth_views.PasswordChangeView.as_view(template_name = 'change_password.html'), name='change_password'),  
    path('change_password_done', auth_views.PasswordResetDoneView.as_view(template_name = 'change_password_done.html'), name='password_change_done'),  
    path('reset_password', auth_views.PasswordResetView.as_view(template_name = "reset_password.html"), name ="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name = "reset_password_sent.html"), name ="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "reset_password_form.html"), name ="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name = "reset_password_done.html"), name ="password_reset_complete"),
]