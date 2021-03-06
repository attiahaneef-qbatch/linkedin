# Generated by Django 3.2.6 on 2021-08-29 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210829_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Connected', 'Connected')], default='Pending', max_length=10)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='myapp.member')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='myapp.member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='connections',
            field=models.ManyToManyField(related_name='_myapp_member_connections_+', through='myapp.Connection', to='myapp.Member'),
        ),
    ]
