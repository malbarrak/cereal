# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('calories', models.IntegerField(max_length=255)),
                ('protein', models.IntegerField(max_length=255)),
                ('fat', models.IntegerField(max_length=255)),
                ('sodium', models.FloatField(max_length=255)),
                ('dietary_fiber', models.FloatField(max_length=255)),
                ('carbs', models.IntegerField(max_length=255)),
                ('sugars', models.IntegerField(max_length=255)),
                ('display_shelf', models.IntegerField(max_length=255)),
                ('potassium', models.IntegerField(max_length=255)),
                ('vitamins_and_minirals', models.IntegerField(max_length=255)),
                ('serving_size_weight', models.FloatField(max_length=255)),
                ('cups_per_serving', models.FloatField(max_length=255)),
            ],
        ),
    ]
