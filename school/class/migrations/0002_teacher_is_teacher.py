# Generated by Django 3.0 on 2021-04-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='is_teacher',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
