from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Coupon
from django.views.decorators.csrf import csrf_exempt
import logging
from django.db import connection


def index_mgg(request):
    shop = request.GET.get('shop')

    query = 'SELECT * FROM listcoupon_coupon WHERE shop_name = %s'
    query_count = 'SELECT COUNT(*) FROM listcoupon_coupon WHERE shop_name = %s'
    list = Coupon.objects.raw(query, [shop])
    with connection.cursor() as cursor:
        cursor.execute(query_count, [shop])
        row = cursor.fetchone()
        count = row[0]

    query = 'SELECT * FROM listcoupon_coupon WHERE shop_name = %s AND type = %s'
    query_count = 'SELECT COUNT(*) FROM listcoupon_coupon WHERE shop_name = %s AND type = %s'
    list_coupon = Coupon.objects.raw(query, [shop, 'coupon'])
    with connection.cursor() as cursor:
        cursor.execute(query_count, [shop, 'coupon'])
        row = cursor.fetchone()
        count_coupon = row[0]

    query = 'SELECT * FROM listcoupon_coupon WHERE shop_name = %s AND type = %s'
    list_deal = Coupon.objects.raw(query, [shop, 'deal'])
    with connection.cursor() as cursor:
        cursor.execute(query_count, [shop, 'deal'])
        row = cursor.fetchone()
        count_deal = row[0]

    content = {
        'countcoupon': count_coupon,
        'countdeal': count_deal,
        'countall': count,
        'shop': shop,
        'listall': list,
        'list_coupon': list_coupon,
        'list_deal': list_deal
    }
    return render(request, "mgg.html", content)

def category(request):
    cat = request.GET.get('category')
    query = 'SELECT * FROM listcoupon_coupon WHERE cate_slugify = %s'
    query_count = 'SELECT COUNT(*) FROM listcoupon_coupon WHERE cate_slugify = %s'
    list = Coupon.objects.raw(query, [cat])
    with connection.cursor() as cursor:
        cursor.execute(query_count, [cat])
        row = cursor.fetchone()
        countall = row[0]

    query = 'SELECT * FROM listcoupon_coupon WHERE cate_slugify = %s AND type = %s'
    query_count = 'SELECT COUNT(*) FROM listcoupon_coupon WHERE cate_slugify = %s AND type = %s'
    list_coupon = Coupon.objects.raw(query, [cat, 'coupon'])
    with connection.cursor() as cursor:
        cursor.execute(query_count, [cat, 'coupon'])
        row = cursor.fetchone()
        countcoupon = row[0]

    query = 'SELECT * FROM listcoupon_coupon WHERE cate_slugify = %s AND type = %s'
    list_deal = Coupon.objects.raw(query, [cat, 'deal'])
    with connection.cursor() as cursor:
        cursor.execute(query_count, [cat, 'deal'])
        row = cursor.fetchone()
        countdeal = row[0]

    cat = list[0].category

    content = {
        'countcoupon': countcoupon,
        'countdeal': countdeal,
        'countall': countall,
        'cat': cat,
        'listall': list,
        'list_coupon': list_coupon,
        'list_deal': list_deal
    }
    return render(request, "category.html", content)
