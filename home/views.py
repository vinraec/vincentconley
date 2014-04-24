from django.shortcuts import render_to_response


def homepage(request):
    return render_to_response('home/home.html')


# Create your views here.
