# Generated by Django 4.0.2 on 2022-03-12 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0005_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(default='image', max_length=200),
        ),
    ]
