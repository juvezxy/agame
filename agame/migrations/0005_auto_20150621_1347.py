# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agame', '0004_auto_20150620_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segment',
            old_name='parent_segment',
            new_name='parent',
        ),
    ]
