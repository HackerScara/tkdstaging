# Generated by Django 2.2.11 on 2020-03-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staging', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='id',
        ),
        migrations.AlterField(
            model_name='stage',
            name='ring',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
