# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('agame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.PositiveIntegerField(default=None, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='lft',
            field=models.PositiveIntegerField(default=None, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='agame.Question', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='rght',
            field=models.PositiveIntegerField(default=None, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='tree_id',
            field=models.PositiveIntegerField(default=None, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='segment',
            name='level',
            field=models.PositiveIntegerField(default=None, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='segment',
            name='lft',
            field=models.PositiveIntegerField(default=None, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='segment',
            name='parent_segment',
            field=mptt.fields.TreeForeignKey(to='agame.Segment', null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='rght',
            field=models.PositiveIntegerField(default=None, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='segment',
            name='tree_id',
            field=models.PositiveIntegerField(default=None, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='segment',
            name='question',
            field=mptt.fields.TreeForeignKey(to='agame.Question', null=True),
        ),
    ]
