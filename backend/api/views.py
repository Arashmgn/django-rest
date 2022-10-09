from django.shortcuts import render

from blog.models import Article
from .serializers import ArticleSerialiser
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
# Create your views here.



class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser
    
    
class ArticleDetail(RetrieveUpdateDestroyAPIView, ):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser
    