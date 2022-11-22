from django.db import models


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    body1 = models.TextField(blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)
    mapimg = models.ImageField(upload_to = "map/", blank=True, null=True)

    def __str__(self):
        return self.start
    
    def summary(self):
        return self.body[:20]

    