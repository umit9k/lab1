from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.contact_list, name='contact_list'),
    url(r'^contact/(?P<pk>\d+)/$', views.contact_detail, name='contact_detail'),
    url(r'^contact/new/$', views.contact_new, name='contact_new'),
    url(r'^contact/(?P<pk>\d+)/edit/$', views.contact_edit, name='contact_edit'),
 ]