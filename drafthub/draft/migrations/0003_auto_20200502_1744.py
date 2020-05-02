# Generated by Django 3.0.5 on 2020-05-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0002_auto_20200501_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='draft',
            options={'ordering': ['-pub_date', '-last_update'], 'verbose_name': 'draft', 'verbose_name_plural': 'drafts'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name=500),
        ),
        migrations.AlterField(
            model_name='draft',
            name='abstract',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='draft',
            name='slug',
            field=models.SlugField(max_length=107),
        ),
        migrations.AlterField(
            model_name='draft',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
