# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .forms import User_Register
from .models import Mall, User, Brand, Store, User_store
from .apps import MyappConfig
import json
import re
from django.http import JsonResponse
from django.http import JsonResponse


# Create your views here.
def show_index(request):
    return render(request, 'index.html')


def show_women(request):
    # print request.path_info
    return render(request, 'women.html')


def show_map(request):
    return render(request, 'map.html')


def show_detail(request):
    return render(request,'details.html')


def show_recommend(request):
    return render(request, 'reconmendation.html')


def show_photos_list(request):
    
    brand = request.GET.getlist('brand[]')
    area = request.GET.getlist('area[]') ###新增area（商区）搜索选项
    discount = request.GET.get('discount')
    dis = re.findall("\d+", discount)
    dis_list = [0,10]
    if len(dis) != 0:
        dis_list[1] = float(dis[0])

    post = []
    for i in range(len(brand)):
        brand_post = Brand.objects.filter(brand_name=brand[i])
        if brand_post:
            post.extend(Store.objects.filter(brand=brand_post[0], on_discount=True))

    for i in range(len(post)):
        mall_post = Mall.objects.filter(pk=post[i].mall.id)
        if mall_post:
            if mall_post[0].mall_in_area not in area:
                post.remove(post[i])

    text_list = []
    for i in range(len(post)):
        if dis_list[0] <= post[i].store_discount < dis_list[1]:
            # print(post[i].brand.brand_image.url[len(MyappConfig.name + '/' + 'static/'):])
            text_list.append({
                'discount': str(post[i].store_discount),
                'brand': post[i].brand.brand_name,
                'store': post[i].store_name,
                'address': post[i].store_location,
                'imgurl': post[i].brand.brand_image.url[len(MyappConfig.name + '/static/'):],
                'jindu': post[i].mall.mall_longitude,
                'weidu': post[i].mall.mall_latitude,
            })
    return HttpResponse(json.dumps(text_list), content_type='application/json')


def checkout(request):
    return render(request,"checkout.html")


def user_register(request):
    if request.method == "POST":
        form = User_Register(request.POST)
        if form.is_valid():
            post = form.save()
            return render(request, 'index.html')
    else:
        form = User_Register()
    return render(request, 'user_register.html')

