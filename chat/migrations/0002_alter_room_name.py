# Generated by Django 4.0.4 on 2022-05-18 06:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.UUIDField(default=uuid.UUID('3d31b83f-7ff2-4ee0-b718-eea864d1e371')),
        ),
    ]