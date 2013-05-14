from django.conf.urls.defaults import *
from django.views.generic.base import TemplateView
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smartshaadi.views.home', name='home'),
    # url(r'^smartshaadi/', include('smartshaadi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                      url(r'^$','friendmakerapp.views.home', name='home'),
                       url(r'^comeback/','friendmakerapp.views.comeback', name='comeback'),
                     # url(r'^admin/', include(admin.site.urls)),
                  

)

