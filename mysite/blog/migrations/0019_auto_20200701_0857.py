# Generated by Django 3.0.7 on 2020-07-01 08:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200701_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 8, 57, 35, 984755, tzinfo=utc)),
        ),
    ]
