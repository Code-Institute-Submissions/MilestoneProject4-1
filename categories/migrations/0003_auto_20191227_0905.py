# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-27 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50),
        ),
    ]
