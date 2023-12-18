"""
URL configuration for finance_track project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from authentication.forms import UserAuthenticationForm
from authentication import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html', authentication_form=UserAuthenticationForm), name='login'),
    path('registration/', views.signup, name='signup'),
    path('authentication/', include('authentication.urls')),
    path('expenses/', include('expenses.urls')),
    path('preferences/', include('user_preferences.urls')),
    path('income/', include('user_income.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
