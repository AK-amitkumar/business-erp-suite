# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-26 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20170426_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='crmlead',
            name='products',
            field=models.ManyToManyField(db_table='lead_products', to='crm.Product'),
        ),
    ]
