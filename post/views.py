
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse
from django.views import View

from .models import PostModel


#function based views
#class based views


# Create your views here.
def post(request):
    return HttpResponse('This is post page')
def detail(request):
    return HttpResponse("This is detail of previous article")
def comments(request):
    if request.method=='GET':
        return HttpResponse("This is GET method of showing comments.")
    if request.method=="POST":
        return HttpResponse("This is POST method of showing comments.")

class Post(View):
     def get(self,request):

         #return HttpResponse("Class based views")
        #şablon
        # articles = [
             # {
             #   'title':'Earthquake happened in Turkiye',
             #   'description':'People out of home',
             #   'date': datetime.now()
             # },
             # {
             #    'title': 'Our diplomats signed contract in China',
             #    'description': 'Business will develop according to these contacts',
             #    'date': datetime.now()
             # }
         #]
         articles=PostModel.objects.order_by('-id').all()
         return render(request,'articles.html',{
             'posts': articles
         })

     #def post(self,request):
      #   return HttpResponse("Post class based views")
class CreatePost(View):
    def get(self,request):
        return render(request,'create_article.html')#url e bind etmeliyik

    def post(self,request):
        title=request.POST.get("title",'unknown')
        description=request.POST.get("description",'unknown')
        date=datetime.now()
        PostModel.objects.create(
            title=title,
            description=description,
            date=date

        )
        return redirect(reverse('list_articles'))