# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-24 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='uid',
            field=models.CharField(max_length=40),
        ),
    ]