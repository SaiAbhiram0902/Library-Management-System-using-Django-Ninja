# Generated by Django 5.0.7 on 2024-07-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='copies',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
