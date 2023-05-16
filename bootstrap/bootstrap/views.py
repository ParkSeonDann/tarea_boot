from django.shortcuts import render
from .listas import *

def inicio(request):
    return render(request, 'index.html')

def mostrar_memes(request):
    context = {
        'titulo':'memes',
        'lista': memes,
    }
    return render(request, 'memes.html', context)

def mostrar_fondos(request):
    context = {
        'titulo':'fondos',
        'lista': fondos,
    }
    return render(request, 'wallpapers.html', context)

def cheems(request):
    return render(request, 'cheems.html')

def mostrar_memes2(request):
    context = {
        'titulo':'memes',
        'lista': memes,
    }
    return render(request, 'coqueto.html', context)