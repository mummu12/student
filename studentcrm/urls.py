"""
URL configuration for studentcrm project.

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from crm.views import StudentCreateView,StudentListView,StudentDetailView,StudentUpdtaeView,StudentDeleteView,SignUpView,SignInView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/add/',StudentCreateView.as_view(),name="stud-add"),
    path('students/all/',StudentListView.as_view(),name="stud-list"),
    path('students/<int:pk>',StudentDetailView.as_view(),name="stud-detail"),
    path('students/<int:pk>/change/',StudentUpdtaeView.as_view(),name="stud-change"),
    path('students/<int:pk>/remove/',StudentDeleteView.as_view(),name="stud-delete"),
    path('registration',SignUpView.as_view(),name="register"),
    path('login',SignInView.as_view(),name="login"),
    path("api/",include("api.urls"))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
