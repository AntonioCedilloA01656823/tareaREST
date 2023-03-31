from django.urls import path
from . import views #se importa clase vista del directorio actual 

urlpatterns = [
    path('',views.index,name='index')
    
]