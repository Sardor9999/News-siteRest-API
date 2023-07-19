from django.shortcuts import render
from requests import request
from .models import *
from django.views.generic import ListView
# Create your views here.

def home(request):
    latest_news = News.objects.filter().order_by(id)[0:1]
    other_news = News.objects.filter().order_by(id)[1:12]
    categories = Category.objects.all()
    regions = Region.objects.all()
    context = {
        'latest_news': latest_news,
        'other_news': other_news,
        categories: categories,
        regions: regions
    }
    return render(request, 'home.html', context)

def detail(request, pk):
    news = News.objects.get(id=id)
    categories = Category.objects.get(id=news.category.id)
    rel_news = News.objects.filter(category=categories).exclude(id=news.id)
    context = {
        'news': news
    }
    return render(request, 'detail.html', context)

class AllNews(ListView):
    model = News
    template_name = 'all_news.html'
    context_object_name = 'all_news'

def category(request):
    categories = Category.objects.get(id=id)
    news = News.objects.filter(category=categories)
    return render(request, 'category.html',
                  {
                      'categories': categories,
                      news: news
                  })

def region(request):
    regions = Region.objects.get(id=id)
    news = News.objects.filter(region=regions)
    return render(request, 'region.html',
                  {
                      'regions': regions,
                      news: news
                  })