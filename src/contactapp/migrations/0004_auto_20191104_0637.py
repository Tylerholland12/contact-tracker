# Generated by Django 2.2.5 on 2019-11-04 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0003_auto_20191104_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
