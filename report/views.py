from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    context = {}
    context['articles'] = models.Article.objects.all().order_by('id')
    context['articles_count'] = models.Article.objects.all().count()
    context['authors_count'] = models.Author.objects.all().count()


    return render(request, 'index.html', context)
    
def news(request, id):
    news = models.Article.objects.get(id=id)

    return render(request, 'projects.html',{
        "news":news
    })

