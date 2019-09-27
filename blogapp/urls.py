from django.urls import path
from .import views

urlpatterns = [
    path('', views.tech_index, name ='index.html'),
    path('contact/', views.contact, name = ''),
    path('category3/', views.category_trois ),
    path('category2/', views.category_deux ),
    path('<int:pk>/', views.category, name = 'category'),
    path('author/', views.author),
    path('single/', views.single),
]