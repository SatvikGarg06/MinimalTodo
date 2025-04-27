"""
URL configuration for todoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse

from django.views.generic.base import RedirectView

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/register/', views.register, name='register'),
    path('login/', RedirectView.as_view(url='/auth/login')),
    path('todos/', views.all_todos, name = 'todos'),
    path('todos/new/', views.new_task, name = "new-task"),
    path("todos/delete/<int:pk>", views.delete_task, name='delete-task'),
    path('todos/edit/<int:pk>', views.edit_task, name='edit-task'),
    path('', views.home, name = 'home'),
]