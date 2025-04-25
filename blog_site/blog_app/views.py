from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm

def home(request):
  post= Post.objects.all()
  context={}
  context["all_posts"]=post

  return render(request,'home.html',context)

