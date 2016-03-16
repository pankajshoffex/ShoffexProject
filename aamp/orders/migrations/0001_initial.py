# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('received', 'Received'), ('dispatched', 'Dispatched'), ('intransist', 'Intransist'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='received', max_length=120)),
                ('shipping_total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=50)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=50)),
                ('payment', models.CharField(blank=True, max_length=120, null=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('type', models.CharField(blank=True, choices=[('billing', 'Billing'), ('shipping', 'Shipping')], default='billing', max_length=120, null=True)),
                ('street', models.TextField()),
                ('postcode', models.CharField(max_length=6)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
    ]
