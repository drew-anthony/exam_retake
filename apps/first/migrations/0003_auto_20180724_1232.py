# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-24 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_quote_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='many',
            new_name='likes',
        ),
    ]
