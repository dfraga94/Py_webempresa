from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

# Create your views here.


def blog(request):
    Blogs = Blog.objects.all()
    return render(request, "blog/blog.html", {'blogs': Blogs})


def category(request, categoryId):
    #category=Category.objects.get(id=categoryId)
    catego=get_object_or_404(Category, id=categoryId)
    # filtar las entradas de acuerdo a la categia
    blogs=Blog.objects.filter(category=catego)
    return render(request ,"blog/category.html",{"blogs":blogs})