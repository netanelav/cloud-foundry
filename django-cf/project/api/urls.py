from django.urls import path

from . import views

urlpatterns = [
    path('create', views.add_message, name='add_message'),
    path('read', views.get_messages, name='get_messages'),
    path('update/<int:id>', views.update_message, name='update_message'),
    path('delete', views.delete_message, name='delete_message'),
]