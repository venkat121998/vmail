# Generated by Django 2.0.3 on 2018-04-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmail', '0005_vmails'),
    ]

    operations = [
        migrations.AddField(
            model_name='vmails',
            name='visit',
            field=models.IntegerField(default=0),
        ),
    ]
