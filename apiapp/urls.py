from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name='api-routes'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('projects/', views.project_list, name='project-list'),
    path('projects/<int:pk>/', views.project_detail, name='project-detail'),
]