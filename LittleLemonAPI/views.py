from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import MenuItem, Cart, Order
from .serializers import MenuItemSerializer, UserSerializer, CartSerializer, OrderSerializer
from django.core.paginator import Paginator, EmptyPage
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.contrib.auth.models import User, Group
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.all()
        to_price = request.GET.get('price')
        search = request.GET.get('search')
        ordering = request.GET.get('ordering')
        perpage = request.GET.get('perpage', default=2)
        page = request.GET.get('page', default=1)
        if to_price:
            items = items.filter(price__lte=to_price)
        if search:
            items = items.filter(title__startswith=search)
        if ordering:
            ordering_fields = ordering.split(',')
            items = items.order_by(*ordering_fields)

        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
        serialized_items = MenuItemSerializer(items, many=True)
        return Response(serialized_items.data)
    elif request.method == 'POST':
        if request.user.groups.filter(name='Manager').exists():
            serialized_item = MenuItemSerializer(data=request.data)
            if serialized_item.is_valid():
                serialized_item.save()
                return Response(serialized_item.data, status=status.HTTP_201_CREATED)
            return Response(serialized_item.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'You are not authorized'}, status.HTTP_403_FORBIDDEN)
    elif request.method == 'PATCH' or request.method == 'PUT' or request.method == 'DELETE':
        if request.user.groups.filter(name='Manager').exists():
            return Response({'message': 'This Request Not Allowed'}, status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            return Response({'message': 'You are not authorized'}, status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'PUT', 'DELETE'])
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def single_menu_items(request, pk):
    if request.method == 'GET':
        item = get_object_or_404(MenuItem, id=pk)
        serialized_item = MenuItemSerializer(item)
        return Response(serialized_item.data)
    else:
        if request.user.groups.filter(name='Manager').exists():
            if request.method == 'PUT':
                try:
                    instance = MenuItem.objects.get(id=pk)
                except MenuItem.DoesNotExist:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

                serialized_item = MenuItemSerializer(
                    instance, data=request.data)
                if serialized_item.is_valid():
                    serialized_item.save()
                    return Response(serialized_item.data)
                return Response(serialized_item.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'DELETE':
                try:
                    instance = MenuItem.objects.get(id=pk)
                except MenuItem.DoesNotExist:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'You are not authorized'}, status.HTTP_403_FORBIDDEN)


# API end-points for SuperUser to add and remove to ManagerGroup
@api_view(['GET', 'POST'])
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def managers(request):
    if request.user.groups.filter(name='Manager').exists():
        if request.method == 'GET':
            managers = User.objects.filter(groups=1)
            # Serialize the managers' data using the UserSerializer
            serialized_data = UserSerializer(managers, many=True).data
            return Response(serialized_data)
        elif request.method == 'POST':
            username = request.POST.get('username')
            if username:
                user = get_object_or_404(User, username=username)
                managers = Group.objects.get(name='Manager')
                managers.user_set.add(user)
                return Response({'message': 'ok'})
            return Response({'message': 'error'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'You are not authorized'}, status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def delete_managers(request, pk):
    if request.user.groups.filter(name='Manager').exists():
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        managers = Group.objects.get(name='Manager')
        managers.user_set.remove(user)
        return Response({'message': 'ok'}, status.HTTP_200_OK)
    else:
        return Response({'message': 'You are not authorized'}, status.HTTP_403_FORBIDDEN)

# API end-points for SuperUser to add and remove to ManagerGroup


@api_view(['GET', 'POST'])
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def deliverycrew(request):
    if request.user.groups.filter(name='Manager').exists():
        if request.method == 'GET':
            managers = User.objects.filter(groups=2)
            # Serialize the managers' data using the UserSerializer
            serialized_data = UserSerializer(managers, many=True).data
            return Response(serialized_data)
        elif request.method == 'POST':
            username = request.POST.get('username')
            if username:
                user = get_object_or_404(User, username=username)
                managers = Group.objects.get(name='DeliveryCrew')
                managers.user_set.add(user)
                return Response({'message': 'ok'})
            return Response({'message': 'error'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'You are not authorized'}, status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def delete_deliverycrew(request, pk):
    if request.user.groups.filter(name='Manager').exists():
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        managers = Group.objects.get(name='DeliveryCrew')
        managers.user_set.remove(user)
        return Response({'message': 'ok'}, status.HTTP_200_OK)
    else:
        return Response({'message': 'You are not authorized'}, status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'POST', 'DELETE'])
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def cart(request):
    token = request.auth
    user_id = request.user.id
    # If belong to Manager or DeliveryCrew Group
    if (request.user.groups.all().exists()):
        return Response({'message': 'You are not authorized'}, status.HTTP_403_FORBIDDEN)
    else:
        if request.method == 'GET':
            # Retrieve the cart for the authenticated user
            cart = get_object_or_404(Cart, user=request.user)

            # Serialize the cart data using your CartSerializer
            serialized_cart = CartSerializer(cart)

            return Response(serialized_cart.data)
        elif request.method == 'POST':
            cart, created = Cart.objects.get_or_create(user=request.user)

            # Get the menu item ID from the request data
            menu_item_id = request.data.get('menu_item_id')

            if not menu_item_id:
                return Response({'message': 'menu_item_id is required'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                # Retrieve the menu item object
                menu_item = MenuItem.objects.get(pk=menu_item_id)
            except MenuItem.DoesNotExist:
                return Response({'message': 'Menu item not found'}, status=status.HTTP_404_NOT_FOUND)

            # Add the menu item to the user's cart
            cart.menu_items.add(menu_item)

            # Serialize and return the updated cart data
            serialized_cart = CartSerializer(cart)
            return Response(serialized_cart.data, status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            cart = get_object_or_404(Cart, user=request.user)
            try:
                cart = Cart.objects.get(user=request.user)
            except Cart.DoesNotExist:
                return Response({'message': 'Cart Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)

            cart.clear_menu_items()
            return Response({'message': 'Cart Cleared'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'message': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'POST'])
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def order(request):
    if request.user.groups.filter(name='Manager').exists():
        if request.method == 'GET':
            orders = Order.objects.all()
            serialized_order = OrderSerializer(orders, many=True)
            return Response(serialized_order.data)
    elif request.user.groups.filter(name='DeliveryCrew').exists():
        if request.method == 'GET':
            delivery_orders = Order.objects.filter(customer=request.user)
            serializer = OrderSerializer(delivery_orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        if request.method == 'GET':
            customer_orders = Order.objects.filter(customer=request.user)
            serializer = OrderSerializer(customer_orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            # Get the current user
            user = request.user

            # Assuming you have a Cart model and a ForeignKey relationship from User to Cart
            # to represent the user's cart
            try:
                cart = Cart.objects.get(user=user)
            except Cart.DoesNotExist:
                return Response({'error': 'Cart does not exist'}, status=status.HTTP_404_NOT_FOUND)

            # Get the menu items from the user's cart
            cart_items = cart.menu_items.all()

            if not cart_items:
                return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

            # Create a new order for the user
            order = Order.objects.create(customer=user)

            # Add the menu items from the cart to the order
            order.items.set(cart_items)

            # Clear the cart by removing all menu items
            cart.menu_items.clear()

            # Serialize the order and return it as a JSON response
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'message': 'You are not authorized'}, status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def single_order(request, pk):
    try:
        instance = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.user.groups.filter(name='Manager').exists():
        if request.method == 'DELETE':
            instance.delete()
            return Response({'message': 'Order Deleted'}, status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            crew_id = request.data.get('delivery_crew_id')
            if crew_id:
                d_crew = User.objects.get(id=crew_id)
                instance.delivery_crew = d_crew
                instance.save()
                serializer = OrderSerializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': 'missing data'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.user.groups.filter(name='Manager').exists() or request.user.groups.filter(name='DeliveryCrew').exists():
        if request.method == 'PATCH':

            # Check if the user making the request is the delivery crew assigned to the order
            if request.user != instance.delivery_crew:
                return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

            # Get the new status value from the request data
            new_status = request.data.get('status')

            # Validate the status value (0 or 1)
            if new_status not in [0, 1]:
                return Response({'error': 'Invalid status value'}, status=status.HTTP_400_BAD_REQUEST)

            # Update the order status
            instance.status = new_status
            instance.save()

            # Serialize the updated order and return it as a JSON response
            serializer = OrderSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        if (instance.customer != request.user):
            return Response({'message': 'You are not authorized'}, status.HTTP_403_FORBIDDEN)

        serializer = OrderSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({'message': 'You are not authorized'}, status.HTTP_403_FORBIDDEN)
