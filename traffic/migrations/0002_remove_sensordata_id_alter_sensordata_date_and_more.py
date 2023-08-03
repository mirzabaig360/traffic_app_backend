# Generated by Django 4.2.3 on 2023-08-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("traffic", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sensordata",
            name="id",
        ),
        migrations.AlterField(
            model_name="sensordata",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="sensordata",
            name="sensor_id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
