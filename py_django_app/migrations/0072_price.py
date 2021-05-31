# Generated by Django 3.2 on 2021-04-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('py_django_app', '0071_alter_room_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_category', models.CharField(choices=[('SINGLE AC', 'SINGLE AC'), ('SINGLE NON-AC', 'SINGLE NON-AC'), ('DOUBLE AC', ' DOUBLE AC'), ('DOUBLE NON-AC', 'DOUBLE NON-AC'), ('TRIPLE AC', 'TRIPLE AC'), ('TRIPLE NON-AC', 'TRIPLE NON-AC'), ('DOUBLE ROOM AC', 'DOUBLE ROOM AC'), ('DOUBLE ROOM NON-AC', 'DOUBLE ROOM NON-AC'), ('FAMILY AC', 'FAMILY AC'), ('KING AC', 'KING AC'), ('DOUBLE-DOUBLE AC', 'DOUBLE-DOUBLE AC'), ('STUDIO', 'STUDIO'), ('PRESIDENT SUITE', 'PRESIDENT SUITE')], max_length=100)),
                ('price', models.CharField(default='0', max_length=30)),
            ],
        ),
    ]
