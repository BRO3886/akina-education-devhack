# Generated by Django 2.2 on 2020-03-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200326_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemrequest',
            name='quantity',
            field=models.CharField(max_length=20),
        ),
    ]