# Generated by Django 3.0.4 on 2020-04-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20200402_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='github_url',
            field=models.CharField(max_length=1100),
        ),
    ]
