from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from .models import Article, Comment, Category
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ArticleForm, CommentForm
from django.http import HttpResponse
from django.contrib import messages
from .decorators import custom_login_required
# Create your views here.


def article_list(request):
    
    articles = Article.objects.all()
    return render(request, 'app/article_list.html', {'articles': articles})


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    form = CommentForm()
    return render(request, 'app/article_detail.html', {'article': article, 'form':form})

@custom_login_required
def add_comment(request, article_id):

    article = get_object_or_404(Article, id = article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)

            comment.user = request.user
            comment.article = article

            comment.save()

            return redirect('article_detail', id=article.id)

    else:
        form = CommentForm()
    
    return render(request, 'app/add_coment.html', {"form": form})


@custom_login_required
@permission_required('blog.add_article', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():

            article = form.save(commit=False)

            article.author = request.user
            article.save()

            return redirect('article_list')
        
    else:
        form = ArticleForm()
    
    return render(request, 'app/create_article.html', {'form': form})


@custom_login_required
@permission_required('blog.change_article', raise_exception=True)
def update_article(request, id):

    article = get_object_or_404(Article, id=id)

    # ownership check
    if request.user != article.author:
        return HttpResponse("Not allowed")

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('article_detail', id=article.id)

    else:
        form = ArticleForm(instance=article)

    return render(request, 'app/update_article.html', {'form': form})

@custom_login_required
@permission_required('blog.delete_article', raise_exception=True)
def delete_article(request, id):

    article = get_object_or_404(Article, id=id)

    
    if request.user != article.author and not request.user.is_superuser:
        return HttpResponse("You are not allowed to delete this article")

    if request.method == 'POST':
        article.delete()
        return redirect('article_list')

    return render(request, 'app/delete_article.html', {'article': article})

@custom_login_required
def delete_comment(request, id):

    comment = get_object_or_404(Comment, id=id)

    # comment owner or admin
    if request.user != comment.user and not request.user.is_superuser:
        return HttpResponse("Not allowed")

    article_id = comment.article.id

    comment.delete()

    return redirect('article_detail', id=article_id)



