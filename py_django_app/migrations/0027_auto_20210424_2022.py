# Generated by Django 2.0.13 on 2021-04-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('py_django_app', '0026_auto_20210424_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='checkintime',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='checkouttime',
            field=models.DateField(null=True),
        ),
    ]
