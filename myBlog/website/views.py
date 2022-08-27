from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from posts.models import Post
from .forms import UserRegisterForm

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html", 
                {"current_time": datetime.now(),
                "posts": Post.objects.all(),
                "num_posts": Post.objects.count(),
                })

def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
    else:
        form = UserRegisterForm()

    return render(request, "registration/signup.html", {"form": form})

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "posts/new.html", {"form": form})