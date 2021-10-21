from django.contrib.postgres import serializers
from django.core.serializers import serialize
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.backends import django
import random

import shop
from .models import *
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

@csrf_exempt
def registration(request):
    model = Users.objects.all()
    login = request.POST['login']
    email = request.POST['email']
    password = request.POST['password']
    for value in model:
        if(value.login != login and value.email != email and model[len(model)-1].id == value.id):
            Users.objects.create(login=login,email=email,password=password)
            return JsonResponse({"result": "вы зарегестрированы"})
            break
        elif(model[len(model)-1].id == value.id):
            return JsonResponse({"result":"вы не зарегестрированы, такой логин или email уже есть"})

@csrf_exempt
def authorization(request):
    model = Users.objects.all()
    login = request.POST['login']
    email = request.POST['email']
    password = request.POST['password']
    for value in model:
        if(value.login == login and value.email == email and value.password == password):
            request.session['login'] = login
            return JsonResponse({"result": "{0} вошли".format(request.session['login'])})
            break
        elif(model[len(model)-1].id == value.id):
            return JsonResponse({"result":"вы не вошли, неправильно введен логин, почта или пароль"})
@csrf_exempt
def all(request):
    try:
        order = request.POST['order']
        page = request.POST['page']
        name = request.POST['name']

        if(id != order):

              goods =  Goods.objects.all().order_by(order)
              if(page == None):
                page = 1
              paginator = Paginator(goods, 4)
              products_paginator = paginator.page(page)
              goods = serialize('json', products_paginator)
              return JsonResponse({"product":goods})
        elif(name != None):
            goods = Goods.objects.filter(name=name)
            result = serialize('json', goods)
            return JsonResponse({"product":goods})
    except:
            goods = Goods.objects.all()
            paginator = Paginator(goods, 4)
            products_paginator = paginator.page(1)
            goods = serialize('json', products_paginator)
            return JsonResponse({"product":goods})


@csrf_exempt
def categories(request,category):

        try:
            cate = Categories.objects.get(name_category=category)
            goods = cate.goods_set.all()
            paginator = Paginator(goods, 4)
            products_paginator = paginator.page(1)
            goods = serialize('json', products_paginator)
            return JsonResponse({"product": goods})
        except shop.models.Categories.DoesNotExist:
            return JsonResponse({"result": "Категории : {0} не существует".format(category)})


@csrf_exempt
def categories_order(request,category,order):
    try:

        cate = Categories.objects.get(name_category=category)
        page = request.POST['page']
        goods = cate.goods_set.all().order_by(order)
        paginator = Paginator(goods, 4)
        products_paginator = paginator.page(page)
        goods = serialize('json', products_paginator)
        return JsonResponse({"product": goods})
    except:
        return JsonResponse({"result": "Категории : {0} не существует или вы неправильно ввели order - {1} ".format(category,order)})

@csrf_exempt
def categories_page(request,category,page):
    try:

        cate = Categories.objects.get(name_category=category)
        goods = cate.goods_set.all()
        paginator = Paginator(goods, 4)
        products_paginator = paginator.page(page)
        goods = serialize('json', products_paginator)
        return JsonResponse({"product": goods})
    except:
        return JsonResponse({"result": "Категории : {0} не существует или вы неправильно ввели order - {1} ".format(category,order)})

@csrf_exempt
def categories_order_page(request,category,order,page):
    try:

        cate = Categories.objects.get(name_category=category)
        goods = cate.goods_set.all().order_by(order)
        paginator = Paginator(goods, 4)
        products_paginator = paginator.page(page)
        goods = serialize('json', products_paginator)
        return JsonResponse({"product": goods})
    except:
        return JsonResponse({"result": "Категории : {0} не существует или вы неправильно ввели order - {1} ".format(category,order)})

@csrf_exempt
def categories_search(request,category):
    try:
        name = request.POST['name']
        cate = Categories.objects.get(name_category=category)
        goods = cate.goods_set.filter(name=name)
        result = serialize('json', goods)
        return JsonResponse({"product":goods})
    except:
        return JsonResponse({"result": "Категории : {0} не существует или вы неправильно ввели name".format(category)})



@csrf_exempt
def grade(request):

    if(request.session['login'] != None):
        id = int(request.POST.get('id'))

        grade_new = int(request.POST.get('grade'))
        goods = Goods.objects.get(pk=id)
        coun = goods.evaluations_set.all().count()
        coun += 1
        grade_old = goods.grade
        result = round(grade_old + (grade_new - grade_old) / coun, 0)
        goods.grade = result
        goods.save()
        goods.evaluations_set.create(name=request.session['login'],grade=grade_new)
        return JsonResponse({"result": "оценка сохранена"})

@csrf_exempt
def orders(request):
    id = request.POST['id']
    num = random.randint(0, 3)
    value = ["в обработке","передан в доставку","исполнен","отменён"]
    good = Goods.objects.get(pk=id)
    user = Users.objects.get(login=request.session['login'])
    user.order_set.create(status=value[num],name_product=good.name_product,
                          description=good.description,image_url=good.image_url,
                          price=good.price,grade=good.grade,tegs=good.tegs)
    return JsonResponse({"result": "заказ сохранён"})

def orders_all(request):

        user = Users.objects.get(login=request.session['login'])
        orders = user.orders_set.all()
        paginator = Paginator(orders, 4)
        products_paginator = paginator.page(1)
        goods = serialize('json', products_paginator)
        return JsonResponse({"product": goods})

























