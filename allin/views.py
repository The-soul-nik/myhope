from django.shortcuts import render
from .models import Article, God



def home(request):

    return render(request, 'allin/home.html')



def articles(request):
    articles = Article.objects.all()
    return render(request, 'allin/article.html', {'articles':articles})



def god(request):
    gods = God.objects.all()
    return render(request, 'allin/gods.html', {'gods':gods})
