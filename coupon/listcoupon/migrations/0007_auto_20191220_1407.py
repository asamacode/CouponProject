# Generated by Django 3.0 on 2019-12-20 07:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listcoupon', '0006_auto_20191218_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='cate_slugify',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 20, 14, 7, 6, 929525), max_length=6),
        ),
    ]
