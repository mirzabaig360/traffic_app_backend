from django.contrib import admin

from traffic.models import SensorData


@admin.register(SensorData)
class AdminSensorData(admin.ModelAdmin):
    list_display = ["sensor_id", "sensor_name", "date"]
