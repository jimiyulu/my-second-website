# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Mall(models.Model):
    AREA_CHOICES = (
        ('海淀区', '海淀区'),
        ('朝阳区', '朝阳区'),
        ('西城区', '西城区'),
        ('东城区', '东城区'),
        ('丰台区', '丰台区'),
        ('昌平区', '昌平区'),
    )
    mall_name = models.CharField(max_length=255, blank=False, null=False)
    mall_in_area = models.CharField(max_length=255, choices=AREA_CHOICES, blank=False, null=False)
    mall_location = models.CharField(max_length=255, blank=False, null=False)
    mall_longitude = models.FloatField(blank=False, null=False)
    mall_latitude = models.FloatField(blank=False, null=False)
    mall_info = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.mall_name


class User(models.Model):
    SEX_CHOICE = (
        ('男', '男'),
        ('女', '女'),
        ('其他', '其他')
    )
    user_id = models.CharField(max_length=11, blank=False, null=False)
    user_name = models.CharField(max_length=255, blank=False, null=False)
    user_sex = models.CharField(max_length=10, choices=SEX_CHOICE, null=True)
    user_password = models.CharField(max_length=255, blank=False, null=False)
    is_business_user = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.user_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=255, blank=False, null=False)
    brand_image = models.ImageField(upload_to='./myapp/static/images/', blank=True, null=True)
    brand_info = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.brand_name


class Store(models.Model):
    business = models.ForeignKey(User)
    brand = models.ForeignKey(Brand)
    mall = models.ForeignKey(Mall)
    store_name = models.CharField(max_length=255, blank=False, null=False)
    store_location = models.CharField(max_length=255, blank=False, null=False)
    on_discount = models.BooleanField(default=False, blank=False, null=False)
    store_discount = models.FloatField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    store_info = models.TextField(blank=True, default='', null=True)

    def __str__(self):
        return self.store_name


class User_store(models.Model):
    user = models.ForeignKey(User)
    store = models.ForeignKey(Store)
    