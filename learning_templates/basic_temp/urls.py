from django.conf.urls import url
from basic_temp import views

# TEMPLATE TAGGING
app_name = 'basic_temp'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
