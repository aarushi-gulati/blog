from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def displayBlogList(request):
    all_posts = Post.objects.all()
    return render(request, 'home.html', {'posts': all_posts})

def displayBlog(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'home.html', {'post': post})

def home(request):
    return HttpResponse('Hehe')
