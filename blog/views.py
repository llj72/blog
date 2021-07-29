from django.http import HttpRequest
from django.shortcuts import render, redirect

from blog.forms import PostForm
from blog.models import Posting


def index(request): #HttpRequest의 객체가 request
    post_list = Posting.objects.all()
    context = {'post_list': post_list}
    return render(request, 'blog/post_list.html', context)

    #return HttpResponse("블로그 메인 페이지입니다.") #응답

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'blog/post_form.html', context)