from django.conf.urls import url
import views

urlpatterns = [

    url(r'^$', views.post_list, name="post_list"),
    url(r'^blog/$', views.post_list, name="post_list"),
    url(r'^blog/stuff/$', views.post_list, name="post_list"),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^post/$', views.new_post, name='new_post'),

]
