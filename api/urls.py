from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("v1/students",views.StudentViewSetView,basename="v1students")
router.register("v2/students",views.StudentViewSetView,basename="v2students")


urlpatterns=[

    path("students/",views.StudentView.as_view()),
    path("students/<int:pk>",views.StudentDetailView.as_view()),
]+router.urls