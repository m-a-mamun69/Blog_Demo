from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts":posts})


# Authentications Stuff
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {"message": "* Username Or Password is Incorrect"}

    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def getPost(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "post_detail.html", {"post":post})

def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('home')


def createPost(request):
    # context = {}
    if request.method == "POST":
        Post.objects.create(
            title = request.POST.get("title"),
            body = request.POST.get("description")
            # author = request.user 
        )
        return redirect('home')
        # except:
        #     context["message"] = "Invalid details"

    return render(request, "new_post.html")


def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    context = {"post":post}
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.body = request.POST.get("description")
        post.save()
        return redirect('home')
    return render(request, "post_update.html", context)

