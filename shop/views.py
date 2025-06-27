from django.shortcuts import render
from shop.forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')

        if request.FILES.get('image'):
            product.image = request.FILES.get('image')

        product.save()
        messages.success(request, "Product updated successfully.")
        return redirect('products')

    return render(request, 'shop/product_form.html', {'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, "Product deleted successfully.")
    return redirect('products')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'


class UserLogoutView(LogoutView):
    next_page = 'login'


class ProductListView(ListView):
    model = Product
    template_name = 'shop/products.html'  # your template file
    context_object_name = 'products'          # variable name in template

def register(request):
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 != password2:
                messages.error(request, "Passwords do not match.")
                return redirect('register')

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
                return redirect('register')

            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
            
        return render(request, 'shop/register.html')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('products')  
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'shop/login.html')

def addproduct(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        stock=request.POST.get('stock')
        image=request.POST.get('image')
        
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            image=image
        )
        messages.success(request, " Successful")
        return redirect('products')  
    return render(request, 'shop/product_form.html')