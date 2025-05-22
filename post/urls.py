from django.contrib import admin
from django.urls import path,include

from .views import post, detail, comments, Post, CreatePost

urlpatterns = [

   path('',post),
   path('detail',detail),
   path('comments',comments),

   path('articles',Post.as_view(),name='list_articles'),
   path('create_article',CreatePost.as_view(),name='create_article')

]
