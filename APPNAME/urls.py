from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path("", home, name="home"),
    path('msg.html', views.new_page_view, name='new_page_view'),
]