# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-21 15:47
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0004_auto_20190421_1156'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeployLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('deploy', 'deploy'), ('rollback', 'rollback')], max_length=12, verbose_name='操作类型')),
                ('tag', models.CharField(default='master', max_length=32, verbose_name='分支或标签名')),
                ('release_name', models.CharField(max_length=128, verbose_name='部署版本')),
                ('release_desc', models.CharField(max_length=128, verbose_name='描述')),
                ('result', models.TextField(verbose_name='执行日志')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='执行时间')),
            ],
            options={
                'verbose_name': '部署记录表',
                'verbose_name_plural': '部署记录表',
                'db_table': 'deploylog',
            },
        ),
        migrations.CreateModel(
            name='ProConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='项目名称')),
                ('env', models.CharField(choices=[('test', '测试环境'), ('pod', '生产环境')], max_length=4, verbose_name='环境')),
                ('checkout_dir', models.CharField(max_length=128, verbose_name='代码检出目录')),
                ('exclude', models.TextField(blank=True, null=True, verbose_name='排除的文件')),
                ('deploy_dir', models.CharField(max_length=128, verbose_name='目标服路径')),
                ('deploy_release', models.CharField(max_length=128, verbose_name='目标服版本地址')),
                ('build_num', models.SmallIntegerField(default=10, verbose_name='版本保留数')),
                ('prev_deploy', models.TextField(blank=True, default='', verbose_name='代码检出前操作')),
                ('post_deploy', models.TextField(blank=True, default='', verbose_name='代码检出后操作')),
                ('prev_release', models.TextField(blank=True, default='', verbose_name='切换版本前操作')),
                ('post_release', models.TextField(blank=True, default='', verbose_name='切换版本后操作')),
                ('versions', models.TextField(blank=True, default='', verbose_name='存储部署过的版本')),
                ('wx_notice', models.BooleanField(default=False, verbose_name='是否开启微信通知')),
                ('to_mail', models.TextField(blank=True, default='', verbose_name='收件人邮箱')),
                ('cc_mail', models.TextField(blank=True, default='', verbose_name='抄送人邮箱')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('deploy_server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Hosts', verbose_name='目标服务器')),
            ],
            options={
                'verbose_name': '项目表',
                'verbose_name_plural': '项目表',
                'db_table': 'proconfig',
            },
        ),
        migrations.CreateModel(
            name='RepoConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_name', models.CharField(max_length=32, verbose_name='仓库名')),
                ('repo_type', models.CharField(choices=[('git', 'git'), ('svn', 'svn')], max_length=3, verbose_name='仓库类型')),
                ('repo_user', models.CharField(max_length=32, verbose_name='账户名')),
                ('repo_password', models.CharField(max_length=64, verbose_name='密码')),
                ('repo_url', models.CharField(max_length=128, verbose_name='仓库地址')),
                ('repo_model', models.CharField(choices=[('brach', 'brach'), ('tag', 'tag'), ('trunk', 'trunk')], max_length=5, verbose_name='版本类型')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '仓库',
                'verbose_name_plural': '仓库',
                'db_table': 'repoconfig',
            },
        ),
        migrations.AddField(
            model_name='proconfig',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='probuild.RepoConfig', verbose_name='仓库'),
        ),
        migrations.AddField(
            model_name='proconfig',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='负责人'),
        ),
        migrations.AddField(
            model_name='deploylog',
            name='pro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='probuild.ProConfig', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='deploylog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='执行者'),
        ),
    ]
