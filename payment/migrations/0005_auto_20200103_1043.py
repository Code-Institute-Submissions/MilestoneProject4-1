# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-03 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20200103_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='bid',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]