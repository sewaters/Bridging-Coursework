from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def home_page(request):
    return render(request, 'blog/home_page.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).exclude(title='CV').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.title == '2019/20 Study Highlights':
        return render(request, 'blog/post_studHigh.html', {'post': post})
    elif post.title == 'My Ambitions for the next Academic Year':
        return render(request, 'blog/post_nextYear.html', {'post': post})
    elif post.title == 'The Structure of my Site and Django Review':
        return render(request, 'blog/post_site&Django.html', {'post': post})
    else:
        return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def CV_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    for p in posts:
        if p.title == 'CV':
            return render(request, 'blog/CV_page.html', {'post': p})

    return render(request, 'blog/CV_page.html')
