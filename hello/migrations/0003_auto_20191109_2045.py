# Generated by Django 2.2.7 on 2019-11-09 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20191109_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basic_itineraries',
            old_name='no_das',
            new_name='no_days',
        ),
        migrations.AddField(
            model_name='basic_itineraries',
            name='total_kms',
            field=models.IntegerField(default=0),
        ),
    ]
