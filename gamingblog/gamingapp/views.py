from django.shortcuts import render
from django.views.generic import ListView
from gamingapp.models import Post

class BlogList(ListView):
    model = Post
    template = 'gamingapp/blog.html'
