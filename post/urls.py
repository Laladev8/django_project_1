from django.contrib import admin
from django.urls import path,include

from .views import post,detail,comments

urlpatterns = [

   path('',post),
   path('detail',detail),
   path('comments',comments),
]
