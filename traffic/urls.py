from django.urls import path
from . import views

urlpatterns = [
    path('dayOfWeekAverageCount', views.day_of_week_average_count, name='day_of_week_average_count'),
]
