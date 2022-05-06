# Generated by Django 3.2.12 on 2022-04-14 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0009_alert_crypto_alert_currency'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='alert',
            name='crypto_alert_currency',
        ),
        migrations.AlterField(
            model_name='alert',
            name='currency',
            field=models.CharField(max_length=30),
        ),
        migrations.AddConstraint(
            model_name='alert',
            constraint=models.CheckConstraint(check=models.Q(('currency__in', ('EUR', 'USD', 'PLN'))), name='crypto_alert_currency'),
        ),
    ]
