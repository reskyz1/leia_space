from django.shortcuts import render
from django.http import HttpRequest

def index(request):
        return render(request, 'galeria/index.html')

def imagem(request):
        return render(request, 'galeria/imagem.html')