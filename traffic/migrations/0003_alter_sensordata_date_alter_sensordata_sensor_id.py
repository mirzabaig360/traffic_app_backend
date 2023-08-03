# Generated by Django 4.2.3 on 2023-08-03 03:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("traffic", "0002_remove_sensordata_id_alter_sensordata_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sensordata",
            name="date",
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name="sensordata",
            name="sensor_id",
            field=models.IntegerField(db_index=True, primary_key=True, serialize=False),
        ),
    ]
