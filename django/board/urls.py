from django.conf.urls import patterns, include, url

urlpatterns = patterns('board.views',
    # Examples:
    # url(r'^$', 'guild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home'),
)
