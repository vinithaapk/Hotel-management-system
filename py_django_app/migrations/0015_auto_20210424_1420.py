# Generated by Django 2.0.13 on 2021-04-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('py_django_app', '0014_auto_20210424_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkintime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkouttime',
            field=models.TimeField(),
        ),
    ]
