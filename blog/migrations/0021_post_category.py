# Generated by Django 3.0 on 2020-05-12 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20200507_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('featured', 'Featured'), ('entertainment', 'Entertainment'), ('news', 'News'), ('tech', 'Technology')], default='entertainment', max_length=20),
        ),
    ]
