from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vincentconley.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', 'blog.views.homepage'),
    url(r'^admin/', include(admin.site.urls)),
)
