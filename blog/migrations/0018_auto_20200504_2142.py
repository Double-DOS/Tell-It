# Generated by Django 3.0 on 2020-05-04 21:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0017_auto_20200504_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favourite',
        ),
        migrations.AddField(
            model_name='post',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]
