# Generated by Django 3.2.9 on 2021-11-17 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20211117_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toad',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]