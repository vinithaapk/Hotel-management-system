# Generated by Django 3.2 on 2021-04-26 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('py_django_app', '0041_rename_contact_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Contact',
        ),
    ]
