# Generated by Django 4.0.2 on 2022-03-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cart_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
