from django.urls import path
from .views import *

urlpatterns = [
    path('registration', registration),
    path('authorization',authorization),
    path('exit',exit),
    path('goods/all/', all),
    path('goods/all/<int:order>', goods_all_order),
    path('goods/all/<int:page>', goods_all_page),
    path('goods/all/<int:order>/<int:page>', goods_all_order_page),
    path('goods/search', goods_search),
    path('goods/categories/<str:category>', categories),
    path('goods/categories/<str:category>/<int:order>', categories_order),
    path('goods/categories/<str:category>/<int:page>', categories_page),
    path('goods/categories/<str:category>/<int:order>/<int:page>', categories_order_page),
    path('goods/categories/<str:category>/search', categories_page),
    path('goods/grade', grade),
    path('goods/orders/create', orders),
    path('goods/orders/all', orders_all),
    path('goods/orders/all/<int:order>', orders_all_order),
    path('goods/orders/all/<int:page>', orders_all_page),
    path('goods/orders/all/<int:order>/<int:page>', orders_all_order_page),
    path('goods/orders/search', orders_search),
    path('goods/favorites/add', favorites_add),
    path('goods/favorites', favorites),


]