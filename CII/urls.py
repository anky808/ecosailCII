from django.urls import path
from CII import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
