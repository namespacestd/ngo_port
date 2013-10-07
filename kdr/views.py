from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from ngo.models import *

import random

def index(request):
    all_posts = NGO_Post.objects.all()
    return render(request, 'index.html', { 'all_posts' : all_posts, 'major_posts' : all_posts.order_by('month') })

def post_page(request):
    cleaned = request.path[6:]
    split = cleaned.split('_')
    ngo = split[0].replace('-', ' ')
    p_id = split[1]
    print ngo
    print p_id

    target_post = NGO_Post.objects.filter(post_id=p_id)
    print target_post[0].title

    all_posts = NGO_Post.objects.all()
    return render(request, 'ngo_post.html', { 'post' : target_post[0], })


def random_elements(num, elements):
    eles = elements.values()
    posts = []
    for element in range(num):
        post_index = int(random.random() * len(eles))
        posts += eles[post_index]
    return posts