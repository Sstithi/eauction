# Generated by Django 2.2.7 on 2019-11-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_message_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sent_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
