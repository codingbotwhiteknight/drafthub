# Generated by Django 3.0.7 on 2020-06-23 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0003_auto_20200623_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='image',
            field=models.URLField(default='https://i.picsum.photos/id/69/1000/1000.jpg?hmac=cz-tN6vUAj05wXXMpqxWaVH5_1jcUooLOWPHKuvOO_E'),
            preserve_default=False,
        ),
    ]
