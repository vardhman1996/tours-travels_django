# -*- coding: utf-8 -*-
from django.db import models


class PackageImages(models.Model):
    image_link = models.ImageField(upload_to='documents/')
    image_text = models.CharField(max_length=10, default='')


class SliderImages(models.Model):
	slider_link = models.ImageField(upload_to='documents/')
	image_caption = models.CharField(max_length=30)