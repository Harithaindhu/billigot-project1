from django.shortcuts import render
from django.http import HttpResponse
import re
# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact-us.html')
def container(request):
    return render(request,'container.html')
def fruits(request):
    return render(request,'fruits.html')
def product(request):
    org_price=request.POST.get('org_price')
    selling_price=request.POST.get('sale_price')
    img=request.POST.get('img')
    product_cat=request.POST.get('product_name')
    p=re.sub(r'[^\w]', ' ', selling_price)
    return render(request,'product_details.html',{'org_price':org_price,'selling_price':selling_price,'img':img,'category':product_cat,'p':p})