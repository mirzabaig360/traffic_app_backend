from django.db import models


class SensorData(models.Model):
    sensor_id = models.IntegerField(primary_key=True, db_index=True)  # Index on sensor_id field
    sensor_name = models.CharField(max_length=100)
    mon_avg_count = models.IntegerField()
    tue_avg_count = models.IntegerField()
    wed_avg_count = models.IntegerField()
    thu_avg_count = models.IntegerField()
    fri_avg_count = models.IntegerField()
    sat_avg_count = models.IntegerField()
    sun_avg_count = models.IntegerField()
    date = models.DateField(db_index=True, auto_now_add=True)  # Index on date field
