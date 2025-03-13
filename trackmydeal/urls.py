"""
URL configuration for gas_utility project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from customerService import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name="AdminPage"),
    
    path('', views.indexPage, name="IndexPage"),
    path('customer/logout/', views.logoutView, name='logout'),
    
    path('login/', views.loginPage, name="LoginPage"),
    path('authenticate/login/', views.login, name="LoginAuthenticate"),
    
    path('register/', views.registerPage, name="RegisterPage"),
    path('authenticate/register/', views.register, name="RegisterAuthenticate"),
    
    path('customer/home/', views.homePage, name="CustomerHomepage"),
    path('customer/account/', views.accountPage, name="CustomerAccountPage"),
    path('customer/update/', views.updateAccount, name='updateAccount'),
    path('customer/change-password/', views.changePassword, name='changePassword'),
    
    path('customer/service/', views.servicePage, name="ServicePage"),    
    path('customer/service/submit/', views.serviceSubmit, name="ServiceSubmit"),    
    
    path('customer/trackservice/', views.trackService, name="TrackService"),
    
    
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)