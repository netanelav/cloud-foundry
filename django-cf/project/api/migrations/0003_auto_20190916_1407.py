# Generated by Django 2.2.5 on 2019-09-16 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190916_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='pub_date',
            new_name='date',
        ),
    ]
