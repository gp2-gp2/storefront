from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse("Hello World")


def say_hello_template(request):
    return render(request, "hello.html")


def say_hello_template_with_context(request):
    return render(
        request, "hello_context.html", {"name": "John", "lastName": "Doe"}
    )
