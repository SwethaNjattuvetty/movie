from django.db import models



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    language = models.CharField(max_length=50)
    images = models.ImageField(upload_to="images", blank=True, null=True)



    def __str__(self):
        return self.title

