from django.contrib import admin
from django.urls import path

from measurement.views import MeasurementView, SensorsView, SensorAdd

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', SensorsView.as_view()),
    path('sensors/', SensorAdd.as_view()),
    # path('sensors/', SensorsView.as_view()),
]
