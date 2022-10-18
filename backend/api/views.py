from django.shortcuts import render
from blog.models import Article
from rest_framework.permissions import IsAdminUser
from .permissions import *
from .serializers import *
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
# Create your views here.



class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    
class ArticleDetail(RetrieveUpdateDestroyAPIView, ):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field     = "pk"
    

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,) 

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser, )