from django.db import models

# Create your models here.
class Movie(models.Model):
    img=models.ImageField(upload_to="moviephoto",default=True,blank=True)
    mname=models.CharField(max_length=90)
    ticket_price=models.IntegerField()
    description=models.TextField()
    Trailer_link=models.CharField(max_length=150)
    language=models.CharField(max_length=50)
    duration=models.BooleanField()
    movie_Type=models.CharField(max_length=50)
    Release_date=models.DateField()