# Generated by Django 5.1.4 on 2024-12-20 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer_name',
        ),
    ]
