# Generated by Django 4.0.4 on 2022-05-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.TextField(default='0db929b4f69b45f887f81e6de50ffc49'),
        ),
    ]
