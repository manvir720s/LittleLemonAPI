# Generated by Django 4.2.5 on 2023-09-09 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0006_rename_carts_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='order_items', to='LittleLemonAPI.menuitem'),
        ),
    ]