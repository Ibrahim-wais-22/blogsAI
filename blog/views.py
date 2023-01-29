from django.shortcuts import render
from .models import Post, Author, Category, Comment, Tag

def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_posts': latest_posts}
    return render(request, 'blog/index.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post, approved=True)
    context = {'post': post, 'comments': comments}
    return render(request, 'blog/post_detail.html', context)

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    posts = Post.objects.filter(author=author)
    context = {'author': author, 'posts': posts}
    return render(request, 'blog/author_detail.html', context)

def category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    posts = Post.objects.filter(categories=category)
    context = {'category': category, 'posts': posts}
    return render(request, 'blog/category_detail.html', context)

def tag_detail(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    posts = tag.posts.all()
    context = {'tag': tag, 'posts': posts}
    return render(request, 'blog/tag_detail.html', context)

