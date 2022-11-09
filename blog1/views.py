from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    return render(request, 'blog1/post_list.html', {
        'Post_list' : qs,
    })