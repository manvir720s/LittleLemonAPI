from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('users/', include('djoser.urls')),
    path('users/', include('djoser.urls.authtoken')),
    path('menu-items/', views.menu_items),
    path('menu-items/<int:pk>', views.single_menu_items),
    path('groups/manager/users/', views.managers),
    path('groups/manager/users/<int:pk>', views.delete_managers),
    path('groups/delivery-crew/users/', views.deliverycrew),
    path('groups/delivery-crew/users/<int:pk>',
         views.delete_deliverycrew),
    path('cart/menu-items/', views.cart),
    path('orders/', views.order),
    path('orders/<int:pk>', views.single_order),
]
