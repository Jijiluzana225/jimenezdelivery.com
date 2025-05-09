# Generated by Django 5.1.4 on 2025-01-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_delete_om_order_instructions_order_money_and_more'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='order',
            name='money',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='store',
            name='open',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
