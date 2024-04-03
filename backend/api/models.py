
from django.db import models

class Video(models.Model):
    file = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Annotation(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='annotations')
    text = models.CharField(max_length=100)
    start_time = models.FloatField()
    end_time = models.FloatField()