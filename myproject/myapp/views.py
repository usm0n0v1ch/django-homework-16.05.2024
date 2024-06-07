from django.shortcuts import render

from myapp.models import Article


# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'myapp/index.html', {'articles': articles})