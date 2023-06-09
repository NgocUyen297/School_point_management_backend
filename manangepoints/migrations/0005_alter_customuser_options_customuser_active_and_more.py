# Generated by Django 4.2 on 2023-04-16 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manangepoints', '0004_cotdiem_hocky_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.AddField(
            model_name='customuser',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='sinhvien',
            name='lop_hoc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sinh_vien', to='manangepoints.lophoc'),
        ),
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together={('email', 'username')},
        ),
    ]
