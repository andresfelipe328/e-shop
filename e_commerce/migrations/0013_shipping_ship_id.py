# Generated by Django 4.0.2 on 2022-03-16 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0012_shipping'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='ship_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
