# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-27 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0009_bidevent_bid_event_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidevent',
            name='bid_event_deadline',
            field=models.DateTimeField(null=True),
        ),
    ]