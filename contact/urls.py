from django.urls import path
from contact import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('contact/<int:contact_id>/detail', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
]
