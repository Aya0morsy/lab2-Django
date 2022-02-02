from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    
]
