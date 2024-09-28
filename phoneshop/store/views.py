from django.shortcuts import render
from .models import Category, Phone


def main_page(request):
    return render(request, 'store/main_page.html')  

def phone_list(request):
    categories = Category.objects.all() 
    phones = Phone.objects.all()  
    return render(request, 'store/phone_list.html', {'categories': categories, 'phones': phones})  
