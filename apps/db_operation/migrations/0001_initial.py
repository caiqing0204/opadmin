# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-19 13:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DbConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.SmallIntegerField(default=3306, verbose_name='端口')),
                ('name', models.CharField(max_length=32, verbose_name='数据库名称')),
                ('user', models.CharField(max_length=32, verbose_name='数据库用户')),
                ('password', models.CharField(max_length=64, verbose_name='数据库密码')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '数据库配置',
                'verbose_name_plural': '数据库配置',
                'db_table': 'dbconfig',
            },
        ),
        migrations.CreateModel(
            name='DbLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sql', models.TextField(verbose_name='执行sql')),
                ('result', models.TextField(verbose_name='执行结果')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='执行时间')),
                ('conf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_operation.DbConfig', verbose_name='DB配置')),
            ],
            options={
                'verbose_name': 'DB日志',
                'verbose_name_plural': 'DB日志',
                'db_table': 'dblogs',
            },
        ),
    ]