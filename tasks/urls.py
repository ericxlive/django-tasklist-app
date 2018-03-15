from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add, name = 'add'),
    path('complete/<task_id>', views.complete, name='complete'),
    path('deletecomplete', views.delete_completed, name='deletecomplete'),
    path('deleteall', views.delete_all, name='deleteall'),
]