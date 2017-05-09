# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from blog import models

# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'author', 'title', 'created_at')