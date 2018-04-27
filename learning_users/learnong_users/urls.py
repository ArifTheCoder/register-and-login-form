
from django.conf.urls import url, include
from django.contrib import admin
from basicApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^basicapp/', include('basicApp.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'special/', views.special, name='special'),
]
