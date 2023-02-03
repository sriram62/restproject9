from .models import Musician,Album
from rest_framework import serializers,fields
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model=Album
        fields=('id','artist_info','name','release_date','rating')
class MusicianSerializer(serializers.ModelSerializer):
    album_musician=AlbumSerializer(read_only=True,many=True)
    class Meta:
        model=Musician
        fields=('id','first_name','last_name','instrument','album_musician')