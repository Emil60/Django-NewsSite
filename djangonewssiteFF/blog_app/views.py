from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post,Category
from django.core.paginator import Paginator

def index(request):
    model1 = Post.objects.all()
    model2 = Category.objects.filter()
    return render(request, "index.html", {"category":model2, "news":model1})
    #paginate_by = 2
# class index(ListView):
#     model = Post,Category
#     template_name = 'index.html'
#     paginate_by = 2

class post(DetailView):
    model = Post
    template_name = 'post.html'


def categorized(request,cat_name):
    model1 = Post.objects.filter(category__cat_name = cat_name)
    model2 = Category.objects.all()
    return render(request, "index.html", {"category":model2, "news":model1})
# Create your views here.
