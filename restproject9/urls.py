"""restproj13 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from rest_framework.authtoken.views import obtain_auth_token
from nestedserializerapp.views import MusiciansList,AlbumsList,MusiciansListById,AlbumsListById

urlpatterns = [
    re_path(r'^api_token_auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
    re_path(r'^api/musicians/$', MusiciansList.as_view()),
    re_path(r'^api/albums/$', AlbumsList.as_view()),
    re_path(r'^api/musicians/(?P<pk>\d+)/$', MusiciansListById.as_view()),
    re_path(r'^api/albums/(?P<pk>\d+)/$', AlbumsListById.as_view()),

]
