# Generated by Django 2.2.6 on 2019-10-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20191018_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='company/default.jpeg', upload_to='profile_pics'),
        ),
    ]
