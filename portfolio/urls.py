from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('add-project/', views.add_project, name='add_project'),
    path('add-skill/', views.add_skill, name='add_skill'), 
    path('contact/', views.contact_view, name= 'contact'),
]