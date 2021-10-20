from django.db import models


class Users(models.Model):
    login = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Categories(models.Model):
    name_category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Goods(models.Model):
    god_cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name_product = models.CharField(max_length=50)
    description = models.CharField(max_length=3000)
    image_url = models.CharField(max_length=300)
    price = models.FloatField()
    grade = models.FloatField()
    tegs = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Favorites(models.Model):
    god_us = models.ForeignKey(Users, on_delete=models.CASCADE)
    name_product = models.CharField(max_length=50)
    description = models.CharField(max_length=3000)
    image_url = models.CharField(max_length=300)
    price = models.FloatField()
    grade = models.FloatField()
    tegs = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Evaluations(models.Model):
    god_grad = models.ForeignKey(Goods, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    grade = models.FloatField()

class Order(models.Model):
    god_order = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    name_product = models.CharField(max_length=50)
    description = models.CharField(max_length=3000)
    image_url = models.CharField(max_length=300)
    price = models.FloatField()
    grade = models.FloatField()
    tegs = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




