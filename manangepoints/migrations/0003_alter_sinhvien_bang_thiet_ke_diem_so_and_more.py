# Generated by Django 4.2 on 2023-04-15 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manangepoints', '0002_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinhvien',
            name='bang_thiet_ke_diem_so',
            field=models.ManyToManyField(null=True, related_name='sinh_viens', through='manangepoints.DiemSo', to='manangepoints.bangthietkediemso'),
        ),
        migrations.AlterField(
            model_name='sinhvien',
            name='lop_hoc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sinh_viens', to='manangepoints.lophoc'),
        ),
    ]
