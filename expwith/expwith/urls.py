from django.conf.urls import patterns, include, url
import register

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'expwith.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^register/', include('register.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
