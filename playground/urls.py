from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.say_hello),
    path("hello-template/", views.say_hello_template),
    path("hello-template-context/", views.say_hello_template_with_context),
    path("debug-test/", views.testing_debug),
]
