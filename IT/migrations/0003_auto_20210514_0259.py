# Generated by Django 3.2 on 2021-05-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0002_auto_20210511_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedata',
            name='des',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='servicedata',
            name='head',
            field=models.CharField(max_length=50),
        ),
    ]
