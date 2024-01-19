from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'variable': "this is about page"
    }
    return render(request, 'about.html', context)

def upload(request):
    context = {
        'variable': "this is upload"
    }
    return render(request, 'upload.html', context)

