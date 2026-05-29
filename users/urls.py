
from django.urls import path
from . import views

urlpatterns = [

    path('', views.landing, name='landing'),

    path('home/', views.home, name='home'),

    path('signup/', views.signup, name='signup'),

    path('login/', views.login, name='login'),

    path('products/', views.products, name='products'),

    path('add-product/',
         views.add_product,
         name='add_product'),

    path('exchange/<int:product_id>/',
         views.exchange,
         name='exchange'),

    path('add-to-cart/<int:product_id>/',
         views.add_to_cart,
         name='add_to_cart'),

    path('cart/',
         views.cart,
         name='cart'),

    path('my-uploads/',
         views.my_uploads,
         name='my_uploads'),

    path('delete-product/<int:product_id>/',
         views.delete_product,
         name='delete_product'),

    path('buy-now/<int:product_id>/',
         views.buy_now,
         name='buy_now'),

    path('my-orders/',
         views.my_orders,
         name='my_orders'),

    path('product/<int:product_id>/',
         views.product_detail,
         name='product_detail'),
    
    path('remove-from-cart/<int:cart_id>/',
        views.remove_from_cart,
        name='remove_from_cart'),
    
    path('delete-product/<int:product_id>/',
        views.delete_product,
        name='delete_product'),
    
    path('cancel-order/<int:order_id>/',
     views.cancel_order,
     name='cancel_order'),
     path(
    'logout/',
    views.logout_user,
    name='logout'
),
     path(
    'exchange-requests/',
    views.exchange_requests,
    name='exchange_requests'
),

 path(
    'delete-exchange-request/<int:request_id>/',
    views.delete_exchange_request,
    name='delete_exchange_request'
),

path(
    'accept-exchange/<int:request_id>/',
    views.accept_exchange,
    name='accept_exchange'
),

path(
    'reject-exchange/<int:request_id>/',
    views.reject_exchange,
    name='reject_exchange'
),

]

