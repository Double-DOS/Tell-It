# Generated by Django 3.0 on 2020-04-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]