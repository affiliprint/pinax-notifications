# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def convert_medium_to_int(apps, schema_editor):
    NoticeSetting = apps.get_model("notifications", "NoticeSetting")
    for n in NoticeSetting.objects.all():
        n.medium_int = int(n.medium)
        n.save()


def convert_medium_to_int_reverse(apps, schema_editor):
    NoticeSetting = apps.get_model("notifications", "NoticeSetting")
    for n in NoticeSetting.objects.all():
        n.medium = str(n.medium_int)
        n.save()


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_add_medium_int'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticesetting',
            name='medium',
        ),
        migrations.RenameField(
            model_name='noticesetting',
            old_name='medium_int',
            new_name='medium',
        ),
        migrations.AlterField(
            model_name='noticesetting',
            name='medium',
            field=models.IntegerField(verbose_name='medium', choices=[(0, b'email')]),
        ),
    ]
