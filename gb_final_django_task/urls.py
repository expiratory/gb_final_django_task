"""
URL configuration for gb_final_django_task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from app.views import index, retrieve_recipe, recipies, add_recipe, CreateUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('recipe/<int:id>/', retrieve_recipe, name='retrieve_recipe'),
    path('recipies/', recipies, name='recipies'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path(
        'recipe/recipe_success_page/',
        TemplateView.as_view(template_name='recipe_success_page.html'),
        name='recipe_success_page'
    ),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', CreateUserView.as_view(), name='registration'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
