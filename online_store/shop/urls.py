from django.urls import path
from .views import *

urlpatterns = [
    path('registration', registration),
    path('authorization',authorization),
    path('goods/all/', all),
    path('goods/categories/<str:category>', categories),
    path('goods/categories/<str:category>/<str:order>', categories_order),
    path('goods/categories/<str:category>/<str:page>', categories_page),
    path('goods/categories/<str:category>/<str:order>/<str:page>', categories_order_page),
    path('goods/categories/<str:category>/search', categories_page),
    path('goods/grade', grade)
]