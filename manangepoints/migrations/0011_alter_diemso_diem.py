# Generated by Django 4.2 on 2023-04-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manangepoints', '0010_alter_bangthietkemonhoc_cot_diem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diemso',
            name='diem',
            field=models.FloatField(default=None, null=True),
        ),
    ]
