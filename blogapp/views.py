from django.shortcuts import render, redirect
from .forms import CreateBlog
from .models import Blog
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def blogMain(request):
    blogs = Blog.objects.all()
    return render(request, 'blogMain.html',{'blogs':blogs})


def createBlog(request):
    if request.method == 'POST':
        form = CreateBlog(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blogMain')
        else:
            return redirect('index')
    else:
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form': form})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)


    return render(request, 'detail.html', {'blog': blog})


#def look(request, blog_id):
 #   blog = get_object_or_404(Blog, pk=blog_id)
  #  select = blog.rank
   # select += 1

    #select.save()

    #return HttpResponseRedirect(reverse('blogMain.html'))

