# Generated by Django 4.0.2 on 2022-03-04 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0020_alter_customer_bill_received_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_item',
            name='Uom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bill_item',
            name='alt_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bill_item',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]