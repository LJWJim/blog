from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
                    #(?P<year>\d+)/(?P<month>\d+)/$
    url(r'^archives/(?P<year>\d+)/(?P<month>\d+)/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'search/$', views.search, name='search'),
]
