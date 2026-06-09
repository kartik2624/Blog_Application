from django.urls import path
from .views import create_article, article_detail, article_list, update_article, add_comment, delete_comment, delete_article

urlpatterns = [
    path('', article_list, name='article_list'),
    path('article/<int:id>/', article_detail, name='article_detail'),
    path('create/', create_article, name='create_article'),
    path('update/<int:id>/', update_article, name='update_article'),
    path('delete-comment/<int:id>/', delete_comment, name='delete_comment'),
    path('add-comment/<int:article_id>/', add_comment, name='add_comment'),
    path('delete_article/<int:id>/', delete_article, name='delete_article'),
]