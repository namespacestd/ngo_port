from django.http import HttpResponse
from django.contrib.auth import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from ngo.models import *
from kdr.forms import *
import uuid

import random

success = False

def index(request):
    all_posts = NGO_Post.objects.all()
    return render(request, 'index.html', { 'all_posts' : append_image_link(all_posts), 'major_posts' : append_image_link(all_posts.order_by('month')) })

def append_image_link(posts):
    appended = []
    for post in posts:
        appended.append({'image_link': post.image, 'post' : post});
    return appended

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
    return render(request, 'ngo_post.html', { 'post' : { 'post' : target_post[0], 'image_link' : target_post[0].image }, })


def random_elements(num, elements):
    eles = elements.values()
    posts = []
    for element in range(num):
        post_index = int(random.random() * len(eles))
        posts += eles[post_index]
    return posts

def admin_page(request):
    all_posts = NGO_Post.objects.all()
    ngos = NGO.objects.all()
    classifications = NGO_Classification.objects.all()
    ngo_image_form = UploadFileForm()
    global success
    prev_success = success

    success = False
    return render(request, 'admin_page.html', { 'is_authenticated' : request.user.is_authenticated, 
                           'current_user' : request.user,
                           'all_posts' : append_image_link(all_posts),
                           'ngos' : ngos,
                           'classifications' : classifications,
                           'ngo_image_form' : ngo_image_form,
                           'success' : prev_success })

def login_request(request):
    if request.method == 'POST':  # If the form has been submitted...
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_authenticated():
            login(request, user)

        return redirect('/admin_page')
    return redirect('/')

def admin_add_parent(request):
    if request.method == 'POST': 
        post = NGO(logo=request.FILES['image'], name=request.POST['ngo_name'], website=request.POST['ngo_site'],)
        post.save()

        global success
        success = True
        return redirect('/admin_page')
    return redirect('/')

def admin_add_ngo(request):
    if request.method == 'POST': 
        target_ngo = NGO.objects.filter(name=request.POST['ngo_parent'])[0]
        classif = []
        for c in request.POST.getlist('ngo_class'):
            classif.append(NGO_Classification.objects.filter(classification=c)[0])
        
        post = NGO_Post(image=request.FILES['image'], title=request.POST['ngo_title'], month=request.POST['ngo_month'], year=int(request.POST['ngo_year']), news=request.POST['ngo_news'], author=request.POST['ngo_author'], ngo=target_ngo)
        post.save()

        for c in classif:
            post.classifications.add(c)
        post.save()
        global success
        success = True
        return redirect('/admin_page')
    return redirect('/')

def admin_delete_ngo(request):
    if request.method == 'POST': 
        target_ngo = NGO_Post.objects.filter(post_id=request.POST['ngo_id'])[0]
        target_ngo.delete()
        return redirect('/admin_page')
    return redirect('/')
