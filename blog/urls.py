from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('post/<str:pk>/', views.getPost, name="post_detail"),
    path('post/<str:pk>/delete/', views.deletePost, name="post_delete"),
    path('new_post/', views.createPost, name="create_post"),
]