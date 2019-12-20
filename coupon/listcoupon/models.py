from django.db import models
from datetime import datetime
# Create your models here.

class Coupon(models.Model):
    title = models.CharField(max_length= 255, default='', unique=True, primary_key= True)
    shop_name = models.CharField(max_length= 255, default='', null=True, blank=True)
    description = models.CharField(max_length= 255, default='', null=True, blank=True)
    date_end = models.DateTimeField(max_length= 6, default= datetime.now())
    voucher = models.CharField(max_length= 20, null=True, blank=True, default= '')
    link = models.CharField(max_length= 255, null=True, blank=True, default= '')
    category = models.CharField(max_length= 255, default='', null=True, blank=True)
    type = models.CharField(max_length= 20, default='', null=True, blank=True)
    value = models.CharField(max_length= 20, default='', null=True, blank=True)
    cate_slugify = models.CharField(max_length= 100, default='', null=True, blank=True)