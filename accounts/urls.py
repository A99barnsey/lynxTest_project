from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('courses/<int:course_id>', views.course, name='course'),
    path('courses', views.courses, name='courses'),
]