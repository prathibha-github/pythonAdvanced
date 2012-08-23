from django.conf.urls import patterns, include, url

from polls.views import index
from polls.views import detail
from polls.views import results
from polls.views import vote
from django.contrib.auth.views import logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^tutorial/', include('tutorial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     
     url(r'^polls/$',index),
     url(r'^polls/(?P<poll_id>\d+)/$',detail),
     url(r'^polls/(?P<poll_id>\d+)/vote/$',vote),
     url(r'^polls/(?P<poll_id>\d+)/results/$',results),
     
     url(r'', include('social_auth.urls')),
     url(r'^polls/logout/$',logout)
)
