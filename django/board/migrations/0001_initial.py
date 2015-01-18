# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('top_point_x', models.IntegerField()),
                ('top_point_y', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
