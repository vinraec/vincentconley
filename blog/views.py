from django.shortcuts import render_to_response
from blog.models import Post, Category


def homepage(request):
    return render_to_response('blog/home.html')


# Create your views here.
