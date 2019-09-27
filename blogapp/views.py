from django.shortcuts import render
from .models import Categorie
from .models import Detail

# Create your views here.

def tech_index(request):
    context={
        'blogapp': Categorie.objects.all()
    } 
    return render(request, 'pages/index.html', context)

def contact(request):
    return render(request, 'pages/contact.html')

def category_trois(request):
    return render(request, 'pages/category3.html')

def category_deux(request):
    return render(request, 'pages/category2.html')

def category(request, pk):
    context = {
        'category':Detail.objects.filter(pk=pk)
    }
    return render(request, 'pages/category.html', context)

def author(request):
    return render(request, 'pages/author.html')

def single(request):
    return render(request, 'pages/single.html')


