import django.shortcuts
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from comments.forms import CommentForm
from django.views.generic import ListView


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    comment_list = post.comment_set.all()
    post.increase_views()

    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)

    return render(request, 'blog/index.html', context={'post_list': post_list})
