# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-17 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_smscodesession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(default='', max_length=64)),
                ('name', models.CharField(default='', max_length=64, null=True)),
                ('email', models.CharField(default='', max_length=128, null=True)),
                ('type', models.CharField(default='user', max_length=128, null=True)),
                ('zhucedi', models.CharField(default='', max_length=256, null=True)),
                ('address', models.CharField(default='', max_length=256, null=True)),
                ('qiyezizhi', models.CharField(default='', max_length=256, null=True)),
                ('chenglanfanwei', models.CharField(default='', max_length=256, null=True)),
                ('lianxiren', models.CharField(default='', max_length=64, null=True)),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
