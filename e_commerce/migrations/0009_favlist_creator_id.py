# Generated by Django 4.0.2 on 2022-03-14 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0008_item_fav_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='favlist',
            name='creator_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
