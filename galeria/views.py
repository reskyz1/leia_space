from django.shortcuts import render
from django.http import HttpRequest



def index(request):
        dados = {
        1:{"nome":"Leia na cama", 
           "legenda":"03/10/2022 - Recife, PE"},
        2:{"nome":"Novo medalhão",
           "legenda":"17/02/2024 - Recife, PE"}
}

        return render(request, 'galeria/index.html', {"cards":dados})

def imagem(request):
        return render(request, 'galeria/imagem.html')