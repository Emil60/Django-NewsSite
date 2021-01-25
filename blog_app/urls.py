from django.urls import path
from .views import index, post
from . import views
urlpatterns = [
    path('', views.index ,name='index'),
    path('post/<int:pk>',post.as_view(),name='post'),
    path('category/<str:cat_name>',views.categorized ,name='categorized'),
]
