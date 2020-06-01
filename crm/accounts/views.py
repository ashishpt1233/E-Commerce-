from django.http import HttpResponse
from django.shortcuts import render
from .models import *



def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customer=  customers.count()
    total_orders=orders.count()
    orders_delivered=Order.objects.filter(status='Delivered').count()
    orders_pending=Order.objects.filter(status='Pending').count()


    context={'orders':orders,'customers':customers,'total_orders':total_orders,'orders_delivered':orders_delivered,'orders_pending':orders_pending}
    return render(request,'accounts/Dashboard.html',context)

def products(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'accounts/products.html',context)

def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    context={'customer':customer}
    return render(request,'accounts/customer.html',context)