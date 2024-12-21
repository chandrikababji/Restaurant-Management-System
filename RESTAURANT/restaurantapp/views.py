import datetime
from django.shortcuts import render
from django.http import JsonResponse
from .models import MenuItem, Orderer, OrderItem
import json
from django.views.decorators.csrf import csrf_exempt

def menu_page(request):
    return render(request, "menu.html")

@csrf_exempt
def place_order(request):
    if request.method == "POST":
         
        data = json.loads(request.body)

   
        total_pric = data.get("total_amount")

        name=data.get("customer")
        dataplace_instance=Orderer(total_price=total_pric,customer_name=name)
        dataplace_instance.save()

    #     order = Order.objects.create(customer_name=customer_name, total_price=total_price)
    #     for item in items:
    #         menu_item = MenuItem.objects.get(id=item['id'])
    #         OrderItem.objects.create(order=order, menu_item=menu_item, quantity=item['quantity'])

    return JsonResponse({"message": "Order placed successfully!"})
