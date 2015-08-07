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
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticesetting',
            name='medium',
            field=models.CharField(null=True, max_length=1, verbose_name='medium', choices=[(0, b'email')]),
        ),
        migrations.AddField(
            model_name='noticesetting',
            name='medium_int',
            field=models.IntegerField(null=True, verbose_name='medium', choices=[(0, b'email')]),
        ),
        migrations.RunPython(convert_medium_to_int, convert_medium_to_int_reverse),
    ]
