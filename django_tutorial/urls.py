from django.conf.urls import patterns, include, url
from helloworld.views import hello, current_datetime
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from books import views


admin.autodiscover()

urlpatterns = patterns('',
                       
                    
    # Examples:
    # url(r'^$', 'django_tutorial.views.home', name='home'),
     ('^hello/$', hello),
     ('^time/$', current_datetime),
     (r'^search-form/$', views.search_form),
     (r'^search/$', views.search),
     (r'^contact-form/$', views.contact),
     (r'^$', views.home_page),
     (r'^thanks/$', views.thanks),
    
     
 
     
     
    
     
     
   
    # url(r'^django_tutorial/', include('django_tutorial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
