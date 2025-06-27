from django.urls import path
from .views import ProductDetailView, UserLogoutView, ProductListView
from . import views # Keep this import for your function-based views

urlpatterns = [
    # This line makes ProductListView the homepage when accessing http://127.0.0.1:8001/
    path('', ProductListView.as_view(), name='home'), # <--- ADD THIS LINE

    # Existing paths
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('products/', ProductListView.as_view(), name='products'), # This can still exist if you want /products/
    path('login/', views.userlogin, name='login'),
    path('register/', views.register, name='register'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product_form/', views.addproduct, name='product_form'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete-product'),
    path('products/update/<int:product_id>/', views.update_product, name='update-product'),
]