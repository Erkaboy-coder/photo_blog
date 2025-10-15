from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def blog_list(request):
    posts = Post.objects.all().order_by('-created_at')
    form = PostForm()
    return render(request, 'blog_list.html', {'posts': posts, 'form': form})

def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('blog_list')
