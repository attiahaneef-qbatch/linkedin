# Generated by Django 3.2.6 on 2021-08-29 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_name',
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
