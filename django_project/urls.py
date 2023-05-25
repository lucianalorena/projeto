"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from appLuciana import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name = "home"),
    path('tasks/', views.list_tasks, name="tasks-list"),
    path('tasks/create/', views.create_task),
    path('musicians/create/', views.create_musician),
    path('tasks/edit/<task_id>', views.update_task),
    path('tasks/delete/<task_id>', views.delete_task),
    path('musicians/', views.list_musician, name="musicians-list"),
    path('musicians/edit/<musician_id>', views.update_musician),
    path('musicians/delete/<musician_id>', views.delete_musician)
  
]

