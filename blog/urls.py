from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('tag/<str:tag_name>/', views.tag_detail, name='tag_detail'),
]
