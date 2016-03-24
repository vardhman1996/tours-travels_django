from django.contrib import admin
from myproject.myapp.models import PackageImages, SliderImages, Package, TestimonialVideo, TestimonialReview



class PackageInline(admin.StackedInline):
	model = Package


class PackageImagesAdmin(admin.ModelAdmin):
	list_display = ('image_text', 'image_link')
	inlines=[PackageInline]

admin.site.register(PackageImages, PackageImagesAdmin)

class SliderImagesAdmin(admin.ModelAdmin):
	list_display = ('image_caption', 'slider_link')


admin.site.register(SliderImages, SliderImagesAdmin)
admin.site.register(TestimonialVideo)

class TestimonialReviewAdmin(admin.ModelAdmin):
	list_display = ('name', 'state', 'tour')

admin.site.register(TestimonialReview, TestimonialReviewAdmin)

