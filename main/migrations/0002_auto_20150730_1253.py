# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition_Facts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calories', models.IntegerField(null=True)),
                ('protein', models.IntegerField(null=True)),
                ('fat', models.IntegerField(null=True)),
                ('sodium', models.FloatField(null=True)),
                ('dietary_fiber', models.FloatField(null=True)),
                ('carbs', models.IntegerField(null=True)),
                ('sugars', models.IntegerField(null=True)),
                ('potassium', models.IntegerField(null=True)),
                ('vitamins_and_minirals', models.IntegerField(null=True)),
                ('serving_size_weight', models.FloatField(null=True)),
                ('cups_per_serving', models.FloatField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='calories',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='carbs',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='cups_per_serving',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='dietary_fiber',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='fat',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='potassium',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='protein',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='serving_size_weight',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='sodium',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='sugars',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='vitamins_and_minirals',
        ),
        migrations.AlterField(
            model_name='cereal',
            name='display_shelf',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(to='main.Manufacturer', null=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='nutrition_facts',
            name='cereal',
            field=models.ForeignKey(to='main.Cereal', null=True),
        ),
    ]
