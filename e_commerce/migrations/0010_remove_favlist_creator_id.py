# Generated by Django 4.0.2 on 2022-03-14 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0009_favlist_creator_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favlist',
            name='creator_id',
        ),
    ]