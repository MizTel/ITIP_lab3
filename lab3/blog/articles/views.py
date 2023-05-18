from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def home(request):
    return HttpResponse(u'Привет, Мир!', content_type="text/plain")


def archive(request):
  return render(request, 'archive.html', {"posts": Article.objects.all()})

# Create your views here.
