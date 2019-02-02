# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-02 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0013_subject_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='batch',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4')], default='A1', max_length=50),
        ),
    ]