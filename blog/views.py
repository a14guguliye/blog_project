from django.shortcuts import render
from  django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic 
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


class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_confirm_delete.html' 
    success_url=reverse_lazy('home')



class SignUpView(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='signup.html'

