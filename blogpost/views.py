from django.shortcuts import render
from django.views.generic import TemplateView

from blogpost.models import Post
# Create your views here.


def homeView(request):
    template = 'index.html'

    posts = Post.objects.select_related("subcategory").select_related("category").select_related("subcategory__category").prefetch_related('like')
    context = {
        
        'posts':posts,
    }
    return render(request, template, context) 