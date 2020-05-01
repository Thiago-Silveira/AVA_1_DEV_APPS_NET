from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'Primeira avaliação': 'Desenvolvimento de Aplicações para a Internet'
    }
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')