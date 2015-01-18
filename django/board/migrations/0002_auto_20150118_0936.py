# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='top_point_x',
        ),
        migrations.RemoveField(
            model_name='mission',
            name='top_point_y',
        ),
    ]
