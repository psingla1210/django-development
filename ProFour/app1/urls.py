from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('other1/', views.other1, name='other1'),
    path('other2/', views.other2, name='other2'),
    path('relative/', views.relative, name='relative'),
]
