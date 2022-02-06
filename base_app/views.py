from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse('Hello World', content_type='text/html')
