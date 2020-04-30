# Generated by Django 2.2 on 2020-03-29 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200326_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=10)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
    ]
