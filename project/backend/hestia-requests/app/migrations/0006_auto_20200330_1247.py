# Generated by Django 2.2 on 2020-03-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_organizations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accepts',
            name='request_id',
            field=models.CharField(max_length=500),
        ),
    ]
