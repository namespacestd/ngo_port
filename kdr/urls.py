from django.conf.urls import patterns, include, url
from kdr.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', index),
	url (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^post.*', post_page),
    url(r'^admin_page', admin_page),
    url(r'^login', login_request),
    url(r'^admin_add_ngo_parent', admin_add_parent),
    url(r'^admin_add_ngo', admin_add_ngo),
    url(r'^admin_delete_ngo', admin_delete_ngo),

    # Examples:
    # url(r'^$', 'kdr.views.home', name='home'),
    # url(r'^kdr/', include('kdr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
