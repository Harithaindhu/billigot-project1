from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name="about"),
    path('gallery',views.gallery,name="gallery"),
    path('contact',views.contact,name="contact"),
    path('container',views.container,name="container"),
    path('fruits',views.fruits,name="fruits"),
    path('product',views.product,name="product"),
]