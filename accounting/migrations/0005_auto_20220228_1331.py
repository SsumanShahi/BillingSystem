# Generated by Django 3.2.12 on 2022-02-28 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_auto_20220228_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledgerdetail',
            name='c_credit_amt',
        ),
        migrations.RemoveField(
            model_name='ledgerdetail',
            name='c_current_date',
        ),
        migrations.RemoveField(
            model_name='ledgerdetail',
            name='c_debt_amt',
        ),
        migrations.RemoveField(
            model_name='ledgerdetail',
            name='c_description',
        ),
        migrations.CreateModel(
            name='ledger_descriptio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_description', models.CharField(max_length=200, null=True)),
                ('c_current_date', models.DateField(null=True)),
                ('c_debt_amt', models.FloatField(null=True)),
                ('c_credit_amt', models.FloatField(null=True)),
                ('ledgerdetail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.ledgerdetail')),
            ],
        ),
    ]
