# Generated by Django 5.1 on 2024-09-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_cart_totals'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]
