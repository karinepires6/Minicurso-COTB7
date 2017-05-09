# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from blog.models import Post

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'post_list.html', {'posts':posts})

def post(request, id):
	posts = Post.objects.filter(id=id)
	return render(request, 'post_list.html', {'posts':posts})