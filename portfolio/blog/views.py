from django.shortcuts import render, get_object_or_404

from.models import Blog

def allblogs(request):
    posts = Blog.objects
    return render(request, 'blog/allblogs.html', {'posts': posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})
