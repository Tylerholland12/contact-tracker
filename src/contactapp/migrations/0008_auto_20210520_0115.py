# Generated by Django 2.2.6 on 2021-05-19 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0007_contact_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='location',
            new_name='contact_location',
        ),
    ]