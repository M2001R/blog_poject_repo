from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .form import PostForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
  post= Post.objects.all()
  context={}
  context["all_posts"]=post

  return render(request,'home.html',context)


class details(DetailView):
  model=Post
  template_name="detailsPage.html"
  
  
class Post_create(CreateView):
  
  model=Post
  
  form_class=PostForm
  
  template_name="Post_create.html"
  success_url=reverse_lazy("home")
  
  
  
 

class post_update(UpdateView):
  model=Post
  form_class=PostForm
  template_name="post_update.html"
  
  
  success_url=reverse_lazy("home")
  
  
class post_delete(DeleteView):
  model=Post
  template_name="post_delete.html"
  success_url=reverse_lazy("home")