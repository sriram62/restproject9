from django.db import models
# Create your models here.
class Musician(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    instrument=models.CharField(max_length=20)
    def __str__(self):
        return self.first_name+" "+self.last_name
class Album(models.Model):
    artist_info=models.ForeignKey(Musician,on_delete=models.CASCADE,related_name='album_musician',null=True,blank=True)
    name=models.CharField(max_length=50)
    release_date=models.DateField()
    rating=models.IntegerField()
    def __str__(self):
        return self.name