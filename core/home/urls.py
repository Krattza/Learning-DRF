from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.post_student, name='student'),
]
