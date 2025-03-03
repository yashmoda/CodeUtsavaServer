# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-04 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Register', '0002_auto_20180203_1510'),
        ('Products', '0002_auto_20180203_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('order_id', models.IntegerField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register.AddressData')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.ProductData')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register.UserData')),
            ],
        ),
    ]
