# Generated by Django 4.2.5 on 2023-09-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0013_alter_order_delivery_crew'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]