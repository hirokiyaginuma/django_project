from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('threads', views.threads, name='threads'),
    path('threads/<int:pk>', views.thread_detail, name='thread_detail'),
    path('deletethread/<int:pk>', views.delete_thread, name='delete_thread'),
    path('deletecomment/<int:th_pk>/<int:cm_pk>', views.delete_comment, name='delete_comment'),
]