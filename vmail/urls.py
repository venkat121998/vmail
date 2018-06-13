from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^index/(?P<id>\d+)/$',views.logouts,name="logout"),
    url(r'^create$',views.create,name='create'),
    url(r'^user/(?P<id>\d+)$',views.user,name="user"),
    url(r'^logins$',views.logins,name='logins'),
    url(r'details/(?P<ide>\d+)/(?P<id>\d+)/$',views.details,name="details"),
    url(r'details_sent/(?P<ide>\d+)/(?P<id>\d+)/$',views.details_sent,name="details_sent"),
    url(r'^compose/(?P<id>\d+)$',views.compose,name="compose"),
    url(r'^sent/(?P<id>\d+)$',views.sent,name="sent")
];
# url(r'^$',views.index,name='index'),
 #   url(r'details/(?P<id>\d+)/$',views.details,name="details"),
  #  url(r'^post/new/$', views.post_new, name='post_new'),
   #  url(r'^search$', views.search, name='search')