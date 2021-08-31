# Generated by Django 3.2.6 on 2021-08-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210830_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='jobs',
            field=models.ManyToManyField(to='myapp.Job'),
        ),
        migrations.AlterField(
            model_name='member',
            name='connections',
            field=models.ManyToManyField(blank=True, through='myapp.Connection', to='myapp.Member'),
        ),
    ]