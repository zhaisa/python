from django.conf.urls import url
from . import views
urlpatterns = [
    # url(r'^$',views.index),
    # url(r'^(\d+)/$',views.detail),
    # url(r'^grades/$',views.grades),
    url(r'^task$',views.gettask),
    url(r'^/mytask/(\d+)/change$',views.geturl)
]