from django.db import models

# Create your models here.
class Memes(models.Model):
    meme_id = models.AutoField
    meme_catagory = models.CharField(max_length=50)
    meme_date = models.DateField()
    image = models.ImageField(upload_to='home/images')
    