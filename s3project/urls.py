"""s3project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from accounts import views as accounts_views
from home import views as home_views
from django.views.static import serve
from .settings import MEDIA_ROOT
from products import views as product_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_index, name='index'),
    url(r'^contact/$', home_views.contact, name='contact'),
	url(r'^register/$', accounts_views.register, name='register'),
	url(r'^profile/$', accounts_views.profile, name='profile'),
	url(r'^login/$', accounts_views.login, name='login'),
	url(r'^logout/$', accounts_views.logout, name='logout'),
	url(r'', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^products/$', product_views.all_products),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^thankyou/$', home_views.get_thanks, name='thankyou'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
