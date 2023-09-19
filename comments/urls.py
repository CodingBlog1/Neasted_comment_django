# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentView.as_view(), name='comment_view'),
]
