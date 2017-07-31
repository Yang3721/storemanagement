# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formNum_de', models.CharField(max_length=30, verbose_name='出库单号')),
                ('operator_re', models.CharField(max_length=30, verbose_name='还库经办人')),
                ('deliveryDate', models.DateField(verbose_name='出库日期')),
                ('returnDate', models.DateField(verbose_name='还库日期')),
                ('type', models.CharField(choices=[('通用测试设备', '通用测试设备'), ('机载测试设备', '机载测试设备'), ('改装装机设备', '改装装机设备'), ('一般耗材', '一般耗材'), ('电连接器', '电连接器'), ('改装标准件', '改装标准件'), ('非标件', '非标件'), ('成品线缆', '成品线缆'), ('系统物资', '系统物资')], max_length=30, verbose_name='出库物品类型')),
                ('storageroom', models.CharField(choices=[('主库房', '主库房'), ('装机库房', '装机库房'), ('隔离库房', '隔离库房')], max_length=30, verbose_name='所属库房')),
                ('manager', models.CharField(max_length=30, verbose_name='库房管理员')),
                ('materialName', models.CharField(max_length=30, verbose_name='物资名称')),
                ('modelNum', models.CharField(max_length=30, verbose_name='物资型号')),
                ('storoomNum', models.CharField(max_length=30, verbose_name='库房编号')),
                ('returnState', models.CharField(max_length=30, verbose_name='还库品状态')),
                ('attachState', models.CharField(max_length=30, verbose_name='附件状态')),
                ('returnNum', models.CharField(max_length=30, verbose_name='还库数量/单位')),
                ('remarks', models.TextField(verbose_name='备注')),
            ],
        ),
    ]