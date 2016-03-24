# -*- coding: utf-8 -*-
from django.db import models
from django.utils.crypto import get_random_string

class SliderImages(models.Model):
	slider_link = models.ImageField(upload_to='slider_images/')
	image_caption = models.CharField(max_length=30)

class PackageImages(models.Model):
    image_link = models.ImageField(upload_to='package_image/')
    image_text = models.CharField(max_length=10, default='')

class Package(models.Model):
	package_name = models.CharField(max_length=30)
	package_image = models.ImageField(upload_to='package_detail_image/')
	package_link = models.OneToOneField(PackageImages, on_delete=models.CASCADE, primary_key=True,)
	package_small_desc = models.CharField(max_length=1000)
	package_modal_link = get_random_string(length=10)
	package_modal_body = models.TextField(max_length=2500)
	package_itenary = models.FileField(upload_to='itenaries/')

class TestimonialVideo(models.Model):
	video_link = models.FileField(upload_to='videos/')