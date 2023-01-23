from django.shortcuts import render

# Create your views here.


def home(request):

    context= {
        'text': 'Hello world',
        'number':100,
    }
    return render(request, 'appfour/home.html', context=context)


def other(request):
    return render(request, 'appfour/other.html')


def relative(request):
    return render(request, 'appfour/relative.html')


def base(request):
    return render(request, 'appfour/base.html')