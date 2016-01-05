
from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import register, login, profile, logout
import core.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core.views.get_index, name='home'),
    url(r'^contact/', 'contact.views.contact', name='contact'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^//logout/$', logout, name='logout'),
]

