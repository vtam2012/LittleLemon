from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('booking/', views.bookingView.as_view()),
    path('menu/', views.menuView.as_view()),
    path('menu/<int:pk>'), views.SingleMenuItemView.as_view())
]