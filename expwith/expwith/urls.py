from django.conf.urls import patterns, include, url
import register
import homepage

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('homepage.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include('register.urls')),
)
