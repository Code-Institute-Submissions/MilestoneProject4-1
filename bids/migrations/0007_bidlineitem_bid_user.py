# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-16 15:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bids', '0006_bidevent_bid_event_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidlineitem',
            name='bid_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]