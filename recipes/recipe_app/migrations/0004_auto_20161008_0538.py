# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0003_auto_20161008_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=20)),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='measurement',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='title',
        ),
        migrations.AddField(
            model_name='recipe',
            name='measurement',
            field=models.ManyToManyField(to='recipe_app.Measurement'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.ManyToManyField(to='recipe_app.RecipeName'),
        ),
    ]
