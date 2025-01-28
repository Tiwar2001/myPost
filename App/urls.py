from django.urls import path
from .import views
from .views import PostListView,PostDetailView,PostUpdateView,PostDeleteView,PostCreateView
urlpatterns = [
    
    path('about/', views.About, name='blog-about'),
    path('', PostListView.as_view(), name="blog-home"),
    path('post/new/',PostCreateView.as_view(),name="blog-new"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="blog-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="blog-delete")
]
