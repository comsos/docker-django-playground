from django.urls import path 
from . import views

urlpatterns = [
    path('send_message/', views.send_message),
    path('messages/', views.show_messages),
    path('reply/<int:id>/',views.reply_to_message,name='reply-to-message')
]