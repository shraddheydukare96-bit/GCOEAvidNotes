# Path: C:\Users\Admin\GCOEAvidNotes\mainsite\urls.py

from django.urls import path
from . import views  # <-- THIS IS THE CORRECT IMPORT

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes_page, name='notes'),
    path('videos/', views.videos_page, name='videos'),
    path('pyqs/', views.pyqs_page, name='pyqs'),
    path('about/', views.about_page, name='about'),
    path('search/', views.search_page, name='search'),
]
