from django.contrib import admin
from .models import Courier, Address, Customer, Package, Shipment, DeliveryStatus, TrackingNumber, Payment


# Courier Admin
class CourierAdmin(admin.ModelAdmin):
    list_display = ('name', 'tracking_number', 'phone_number', 'email', 'is_active')
    search_fields = ('name', 'tracking_number', 'email')
    list_filter = ('is_active',)
    ordering = ('name',)

admin.site.register(Courier, CourierAdmin)


# Address Admin
class AddressAdmin(admin.ModelAdmin):
    list_display = ('line1', 'city', 'state', 'postal_code', 'country')
    search_fields = ('line1', 'city', 'state', 'postal_code', 'country')
    list_filter = ('country',)
    ordering = ('city',)

admin.site.register(Address, AddressAdmin)


# Customer Admin
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('email',)
    ordering = ('last_name',)

admin.site.register(Customer, CustomerAdmin)


# Package Admin
class PackageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'weight', 'dimensions', 'value')
    search_fields = ('sender__first_name', 'receiver__first_name', 'weight', 'dimensions')
    list_filter = ('sender', 'receiver')
    ordering = ('weight',)

admin.site.register(Package, PackageAdmin)


# Shipment Admin
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('package', 'courier', 'scheduled_pickup', 'actual_pickup', 'scheduled_delivery', 'status')
    search_fields = ('package__sender__first_name', 'package__receiver__first_name', 'courier__name')
    list_filter = ('status', 'courier', 'scheduled_pickup', 'scheduled_delivery')
    ordering = ('scheduled_pickup',)

admin.site.register(Shipment, ShipmentAdmin)


# Delivery Status Admin
class DeliveryStatusAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'status', 'timestamp', 'notes')
    search_fields = ('shipment__package__sender__first_name', 'shipment__package__receiver__first_name', 'status')
    list_filter = ('status',)
    ordering = ('timestamp',)

admin.site.register(DeliveryStatus, DeliveryStatusAdmin)


# Tracking Number Admin
class TrackingNumberAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'tracking_code')
    search_fields = ('tracking_code', 'shipment__package__sender__first_name')
    ordering = ('shipment',)

admin.site.register(TrackingNumber, TrackingNumberAdmin)


# Payment Admin
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'amount', 'payment_date', 'payment_method')
    search_fields = ('shipment__package__sender__first_name', 'amount', 'payment_method')
    list_filter = ('payment_method',)
    ordering = ('payment_date',)

admin.site.register(Payment, PaymentAdmin)

