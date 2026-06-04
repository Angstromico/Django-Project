from django.urls import path
from .views import hello_word, HelloView

urlpatterns = [
    path('hello/', hello_word, name='hello_word'),
    path('hello-class/', HelloView.as_view(), name='hello_class'),
]