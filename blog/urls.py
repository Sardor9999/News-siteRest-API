from django.urls import path
from .views import category_list, category_detail, PostListCreateAPIView, category_create, category_delete, PostDetailUpdateDeleteAPIView

urlpatterns = [
    path('create/cat/', category_create, name="category_create"),
    path('cats/', category_list, name="api_main"),
    path('cat/<slug:slug>/', category_detail, name="category_detail"),
    path('cat/delete/<slug:slug>/', category_delete, name="category_delete"),
    path('posts/', PostListCreateAPIView.as_view(), name="post_list_crate_view"),
    path('post/<slug:slug>/', PostDetailUpdateDeleteAPIView.as_view(), name="post_detail"),
]
