# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import PackageImages, SliderImages, Package



def index(request):
    images = PackageImages.objects.all()
    slider_images = SliderImages.objects.all()
    packages = Package.objects.all()
    # Render list page with the documents and the form
    return render_to_response(
        'index.html',
        
        {
         'images': images, 
         'slider_images': slider_images,
         'packages': packages
        },

        context_instance=RequestContext(request)
    )
