import uuid
from django.db import models

# Courier Model
class Courier(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    tracking_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.name} - Tracking No: {self.tracking_number}"

# Address Model
class Address(models.Model):
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.line1}, {self.city}, {self.state}, {self.country}"


# Customer Model
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Package Model
class Package(models.Model):
    weight = models.FloatField()  # In kg or any unit
    dimensions = models.CharField(max_length=255)  # e.g. LxWxH in cm or inches
    description = models.TextField(null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sender = models.ForeignKey(Customer, related_name='sent_packages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Customer, related_name='received_packages', on_delete=models.CASCADE)

    def __str__(self):
        return f"Package for {self.receiver} - {self.weight}kg"


# Shipment Model
class Shipment(models.Model):
    package = models.ForeignKey(Package, related_name='shipments', on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, related_name='shipments', on_delete=models.CASCADE)
    pickup_address = models.ForeignKey(Address, related_name='pickup_addresses', on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(Address, related_name='delivery_addresses', on_delete=models.CASCADE)
    scheduled_pickup = models.DateTimeField()
    actual_pickup = models.DateTimeField(null=True, blank=True)
    scheduled_delivery = models.DateTimeField()
    actual_delivery = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('In Transit', 'In Transit'), 
                 ('Delivered', 'Delivered'), ('Failed', 'Failed')],
        default='Pending'
    )

    def __str__(self):
        return f"Shipment of {self.package} by {self.courier} from {self.pickup_address.city} to {self.delivery_address.city}"


# Delivery Status Model
class DeliveryStatus(models.Model):
    shipment = models.ForeignKey(Shipment, related_name='status_updates', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('In Transit', 'In Transit'), 
                 ('Delivered', 'Delivered'), ('Failed', 'Failed')],
        default='Pending'
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.status} - {self.shipment.package} at {self.timestamp}"


# Tracking Number Model
class TrackingNumber(models.Model):
    shipment = models.OneToOneField(Shipment, related_name='tracking_number', on_delete=models.CASCADE)
    tracking_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Tracking Number: {self.tracking_code} for {self.shipment.package}"

# Payment Model (Optional)
class Payment(models.Model):
    shipment = models.ForeignKey(Shipment, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100, choices=[('Credit Card', 'Credit Card'), 
                                                              ('Cash', 'Cash'), 
                                                              ('PayPal', 'PayPal')])

    def __str__(self):
        return f"Payment of {self.amount} for shipment {self.shipment.id}"
