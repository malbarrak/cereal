# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150730_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition_facts',
            name='carbs',
            field=models.FloatField(null=True),
        ),
    ]
