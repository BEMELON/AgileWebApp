# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-27 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startPage', '0004_auto_20170724_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_contents',
            field=models.CharField(default='', max_length=40),
        ),
    ]
