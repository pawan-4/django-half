from django.utils import timezone
from  django.shortcuts import render, get_object_or_404 ,redirect
from .forms import  * 
from .models import *
from django.contrib.auth import login 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , authenticate
from collections import Counter
from django.contrib.auth import logout

def post_list(request, category_slug=None):
    posts = Post.objects.all().order_by('published_date')
    print(posts)

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

 

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def category_post(request, slug):
    category = Post.objects.filter(category__slug = slug)
    print(category)
    return render(request, 'blog/post_list.html', {'posts': category})
 
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})

def tag_post(request, slug):
    tag = Post.objects.filter(tags__slug = Tag.objects.filter(slug=slug).last())
    
    return render(request,'blog/post_list.html', {'posts': tag})
  
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')  
    else:
        form = LoginForm()
    return render(request, 'blog/user_login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('blog/user_login.html') 

def user_detail(request, user_id):
    print(user_id)
    print("---------")
    user = User.objects.get(id=user_id)
    
    return render(request, 'blog/user_detail.html', {'user': user})

def edit_view(request, pk):
    instance = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = User(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('user_detail', pk=pk)  
    else:
        form = User(instance=instance)

    return render(request, 'user_edit.html', {'form': form})