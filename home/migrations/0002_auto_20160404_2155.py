# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 02:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='header_background_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='logo_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='s1_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='service_2_price',
            field=models.IntegerField(default=289),
        ),
        migrations.AlterField(
            model_name='icon',
            name='style',
            field=models.IntegerField(),
        ),
    ]
