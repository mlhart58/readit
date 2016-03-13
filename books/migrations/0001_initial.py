# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=70)),
                ('review', models.TextField(blank=True, null=True)),
                ('date_reviewed', models.DateTimeField(blank=True, null=True)),
                ('is_favourite', models.BooleanField(default=False)),
            ],
        ),
    ]
