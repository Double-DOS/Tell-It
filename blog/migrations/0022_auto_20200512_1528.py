# Generated by Django 3.0 on 2020-05-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('entertainment', 'Entertainment'), ('news', 'News'), ('tech', 'Technology')], default='entertainment', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('featured', 'Featured')], default='draft', max_length=10),
        ),
    ]
