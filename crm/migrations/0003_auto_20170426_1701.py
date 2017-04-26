# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-26 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20170408_1604'),
        ('crm', '0002_auto_20170326_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrmOpportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=300, verbose_name='Subject')),
                ('stage', models.CharField(max_length=10, verbose_name='Stage')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Customer', verbose_name='Custommer')),
            ],
        ),
        migrations.AlterField(
            model_name='crmlead',
            name='fax',
            field=models.IntegerField(blank=True, null=True, verbose_name='Fax'),
        ),
        migrations.AlterField(
            model_name='crmlead',
            name='stage',
            field=models.CharField(choices=[('new', 'New'), ('progress', 'In progress'), ('matured', 'Matured'), ('dead', 'Dead')], default='new', max_length=10, verbose_name='Stage'),
        ),
    ]
