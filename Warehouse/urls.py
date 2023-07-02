from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from basic import views as core_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/', core_views.signup, name='signup'),
    url(r'^login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^aboutus/', include('aboutus.urls')),
    url(r'^store/', include('store.urls')),
    url(r'^more/', include('more.urls')),
    url(r'^sell/', include('sell.urls')),
    url(r'^buy/', include('buy.urls')),
    url(r'^', include('basic.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)