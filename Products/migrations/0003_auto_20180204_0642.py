# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-04 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_auto_20180203_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdata',
            name='name_eng',
            field=models.TextField(),
        ),
    ]
