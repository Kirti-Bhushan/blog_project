from django.contrib import admin
from blogapp.models import blogPost,Comment

# Register your models here.
admin.site.register(blogPost)
admin.site.register(Comment)
