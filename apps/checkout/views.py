from oscar.apps.checkout.views import ShippingAddressView

class ShippingAddress(ShippingAddressView):
    template_name = 'oscar/checkout/shipping_address.html'