from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic import View
from .models import Article
# Create your views here.

class articleList(ListView):
    
    def get_queryset(self):
        
        return Article.objects.filter(status=True)
        
   
