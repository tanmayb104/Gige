# Generated by Django 3.1.7 on 2021-04-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210316_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default=0, upload_to='profile_pic'),
            preserve_default=False,
        ),
    ]
