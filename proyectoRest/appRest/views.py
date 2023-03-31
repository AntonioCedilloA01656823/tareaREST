from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios,Partidas
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
import sqlite3 
import requests

# Create your views here.
def index(request):
    print("inicio")
    return "pagina de servicio rest"