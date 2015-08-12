# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150730_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(default=2, unique=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nutrition_facts',
            name='cereal',
            field=models.OneToOneField(null=True, to='main.Cereal'),
        ),
    ]
