# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('agame', '0003_auto_20150620_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='agame.Question', null=True),
        ),
    ]
