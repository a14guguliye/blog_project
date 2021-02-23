from django.shortcuts import render
from  django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from .models import *
# Create your views here.
class BlogListView(ListView):
    model=Post
    template_name='home.html'
    

class BlogDetailView(DetailView):
    model=Post
    template_name='post_detail.html'
    context_object_name='post'



class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields='__all__'


class BlogUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body']