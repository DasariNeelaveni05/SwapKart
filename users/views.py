from products.models import ExchangeRequest
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

from django.contrib.auth.decorators import login_required

from products.models import Product, Cart, Order


def landing(request):
    return render(request, 'landing.html')



@login_required
def home(request):

    products = Product.objects.all().order_by('-created_at')

    return render(request, 'home.html', {
        'products': products
    })




def signup(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login/')

    return render(request, 'signup.html')


def login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            return redirect('/home/')

        else:

            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')


@login_required
def add_product(request):

    if request.method == "POST":

        title = request.POST.get('title')

        description = request.POST.get('description')

        price = request.POST.get('price')

        category = request.POST.get('category')

        exchange_value = request.POST.get('exchange')

        image = request.FILES.get('image')

        exchange = False

        if exchange_value == "Yes":
            exchange = True

        Product.objects.create(
            user=request.user,
            title=title,
            description=description,
            price=price,
            category=category,
            exchange=exchange,
            image=image
        )

        return redirect('/products/')

    return render(request, 'add_product.html')


def products(request):

    search = request.GET.get('search')

    products = Product.objects.all()

    if search:
        products = products.filter(
            title__icontains=search
        )

    products = products.order_by('-created_at')

    return render(request,
                  'products.html',
                  {
                      'products': products
                  })


@login_required
def exchange(request, product_id):

    product = Product.objects.get(id=product_id)

    if request.method == "POST":

        message = request.POST.get('message')

        offered_product = request.POST.get(
            'offered_product'
        )

        phone = request.POST.get(
            'phone'
        )

        condition = request.POST.get(
            'condition'
        )

        exchange_image = request.FILES.get(
            'exchange_image'
        )

        ExchangeRequest.objects.create(

            product=product,

            requester=request.user,

            offered_product=offered_product,

            phone=phone,

            condition=condition,

            exchange_image=exchange_image,

            message=message

        )

        return redirect('/exchange-requests/')

    return render(
        request,
        'exchange.html',
        {
            'product': product
        }
    )



@login_required
def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    already_in_cart = Cart.objects.filter(
        user=request.user,
        product=product
    ).exists()

    if not already_in_cart:

        Cart.objects.create(
            user=request.user,
            product=product
        )

    return redirect('/cart/')




@login_required
def cart(request):

    cart_items = Cart.objects.filter(user=request.user)

    return render(request, 'cart.html', {
        'cart_items': cart_items
    })


@login_required
def remove_from_cart(request, cart_id):

    cart_item = Cart.objects.get(id=cart_id)

    if cart_item.user == request.user:
        cart_item.delete()

    return redirect('/cart/')




@login_required
def buy_now(request, product_id):

    product = Product.objects.get(id=product_id)

    if request.method == "POST":

        Order.objects.create(
            user=request.user,
            product=product
        )

        return redirect('/my-orders/')

    return render(request,
                  'payment.html',
                  {
                      'product': product
                  })



    return redirect('/my-orders/')

@login_required
def my_orders(request):

    orders = Order.objects.filter(user=request.user)

    return render(request, 'my_orders.html', {
        'orders': orders
    })

@login_required
def cancel_order(request, order_id):

    order = Order.objects.get(id=order_id)

    if order.user == request.user:
        order.delete()

    return redirect('/my-orders/')




@login_required
def my_uploads(request):

    products = Product.objects.filter(
        user=request.user
    )

    return render(request,
                  'my_uploads.html',
                  {
                      'products': products
                  })


@login_required
def delete_product(request, product_id):

    product = Product.objects.get(id=product_id)

    if product.user == request.user:
        product.delete()

    return redirect('/homes/')




@login_required
def delete_product(request, product_id):

    product = Product.objects.get(id=product_id)

    if product.user == request.user:
        product.delete()

    return redirect('/my-uploads/')


def product_detail(request, product_id):

    product = Product.objects.get(id=product_id)

    return render(request,
                  'product_detail.html',
                  {
                      'product': product
                  })
def logout_user(request):

    logout(request)

    return redirect('/')

@login_required
def exchange_requests(request):

    received_requests = ExchangeRequest.objects.filter(
        product__user=request.user
    ).order_by('-created_at')

    sent_requests = ExchangeRequest.objects.filter(
        requester=request.user
    ).order_by('-created_at')

    return render(
        request,
        'exchange_requests.html',
        {
            'received_requests': received_requests,
            'sent_requests': sent_requests,
        }
    )

@login_required
def delete_exchange_request(request, request_id):

    exchange_request = ExchangeRequest.objects.get(
        id=request_id
    )

    if exchange_request.requester == request.user:

        exchange_request.delete()

    return redirect('/exchange-requests/')

@login_required
def accept_exchange(request, request_id):

    exchange_request = ExchangeRequest.objects.get(
        id=request_id
    )

    if exchange_request.product.user == request.user:

        exchange_request.status = "Accepted"

        exchange_request.save()

    return redirect('/exchange-requests/')


@login_required
def reject_exchange(request, request_id):

    exchange_request = ExchangeRequest.objects.get(
        id=request_id
    )

    if exchange_request.product.user == request.user:

        exchange_request.status = "Rejected"

        exchange_request.save()

    return redirect('/exchange-requests/')