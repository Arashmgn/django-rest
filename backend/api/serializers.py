from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields =("title", "slug", "author",
        #         "content", "publish" ,
        #         "status")
        fields = "__all__"
        # exclude = ('updated','created')
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields =("title", "slug", "author",
        #         "content", "publish" ,
        #         "status")
        fields = "__all__"
        # exclude = ('updated','created')