from decimal import Decimal

import stripe

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


def item_list(request):
    items = Item.objects.all().order_by("-id")

    return render(
        request,
        "shop/item_list.html",
        {
            "items": items,
        },
    )


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)

    return render(
        request,
        "shop/item_detail.html",
        {
            "item": item,
            "stripe_public_key": settings.STRIPE_PUBLISHABLE_KEY,
        },
    )


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)

    image_url = None

    if item.image:
        image_url = request.build_absolute_uri(item.image.url)

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": item.currency,
                        "product_data": {
                            "name": item.name,
                            "description": item.description,
                            "images": [image_url] if image_url else [],
                        },
                        "unit_amount": int(item.price * Decimal("100")),
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=f"{settings.DOMAIN}/success/",
            cancel_url=f"{settings.DOMAIN}/cancel/",
        )

        return JsonResponse({"id": checkout_session.id})

    except stripe.StripeError as error:
        return JsonResponse(
            {"error": str(error)},
            status=500,
        )

def success(request):
    return render(request, "shop/success.html")


def cancel(request):
    return render(request, "shop/cancel.html")

def home(request):
    return redirect("item_detail", id=1)