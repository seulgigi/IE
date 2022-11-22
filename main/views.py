from django.shortcuts import render,redirect, get_object_or_404
from .models import Blog
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def showmain(request):
    blogs = Blog.objects.all()
    return render(request, 'main/mainpage.html',{'blogs':blogs})



def detail(request,id):
    blog = get_object_or_404(Blog ,pk=id)
    return render(request, 'main/detail.html', {'blog':blog})

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_blog = Blog()
    new_blog.start = request.POST['start']
    new_blog.end = request.POST['end']
    new_blog.body = request.POST['body']
    new_blog.body1 = request.POST['body1']
    new_blog.body2 = request.POST['body2']
    new_blog.image =request.FILES.get('image')
    new_blog.mapimg =request.FILES.get('mapimg')
    new_blog.save()
    return redirect('detail', new_blog.id)

def search(request):
    blogs = Blog.objects.all().order_by('-id')
    q = request.POST.get('q',"")

    if q:
        blogs = blogs.filter(start__icontains=q)
        return render(request, 'search.html',{'blogs' : blogs, 'q' : q})

    else:
        return render(request, 'search.html')

