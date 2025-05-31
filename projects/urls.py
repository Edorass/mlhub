from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('add/', views.add_project, name='add_project'),
    path('edit/<int:pk>/', views.edit_project, name='edit_project'),
    path('delete/<int:pk>/', views.delete_project, name='delete_project'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('register/', views.register, name='register')
]
