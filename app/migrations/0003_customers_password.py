# Generated by Django 4.2.1 on 2023-08-21 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customers_customer_cpr_customers_pin_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='password',
            field=models.CharField(default='', max_length=10),
        ),
    ]