"""
URL configuration for arrow_rsc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static  

urlpatterns = [
    path('vacancy/', include('vacancy.urls', namespace = 'vacancy')),
    path('info/', include('info_pages.urls', namespace = 'info')),
    path('', include('vacancy.urls', namespace='vacancy_main')),
    path('tinymce/', include('tinymce.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls)
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
