# Generated by Django 2.2.5 on 2019-11-04 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0002_auto_20191103_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]