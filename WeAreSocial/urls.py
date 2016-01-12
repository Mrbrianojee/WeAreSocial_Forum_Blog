from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import register, login, profile, logout
import core.views
import threads.views
from .settings import MEDIA_ROOT
import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core.views.get_index, name='home'),
    url(r'^contact/', 'contact.views.contact', name='contact'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^//logout/$', logout, name='logout'),

    # forum additions
    url(r'^forum/', threads.views.forum, name='forum'),
    url(r'^threads/(?P<subject_id>\d+)/$', threads.views.threads, name='threads'),
    url(r'^thread/(?P<thread_id>\d+)/$', threads.views.thread, name='thread'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', threads.views.new_thread, name='new_thread'),

    url(r'^post/new/(?P<thread_id>\d+)/$', threads.views.new_post, name='new_post'),

    url(r'^post/delete_post/(?P<post_id>\d+)/$', threads.views.delete_post, name='delete_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', threads.views.edit_post, name='edit_post'),

    # blog additions
    url(r'', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
