from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=200)
    website = models.URLField(max_length=100)
    def __str__(self):
        return self.name



class WatchList(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title