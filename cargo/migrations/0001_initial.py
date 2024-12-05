# Generated by Django 5.1.1 on 2024-11-23 10:43

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=255)),
                ('line2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('tracking_number', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('dimensions', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_packages', to='cargo.customer')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_packages', to='cargo.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_pickup', models.DateTimeField()),
                ('actual_pickup', models.DateTimeField(blank=True, null=True)),
                ('scheduled_delivery', models.DateTimeField()),
                ('actual_delivery', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered'), ('Failed', 'Failed')], default='Pending', max_length=20)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='cargo.courier')),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_addresses', to='cargo.address')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='cargo.package')),
                ('pickup_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup_addresses', to='cargo.address')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(choices=[('Credit Card', 'Credit Card'), ('Cash', 'Cash'), ('PayPal', 'PayPal')], max_length=100)),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='cargo.shipment')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered'), ('Failed', 'Failed')], default='Pending', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_updates', to='cargo.shipment')),
            ],
        ),
        migrations.CreateModel(
            name='TrackingNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_code', models.CharField(max_length=50, unique=True)),
                ('shipment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tracking_number', to='cargo.shipment')),
            ],
        ),
    ]
