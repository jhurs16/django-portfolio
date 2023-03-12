from django.db import models
from enum import unique
import uuid
from django.utils.translation import gettext_lazy as _
def upload_to(instance, filename):
    return 'projects/{filename}'.format(filename=filename)
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=200, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="projects/default.jpg", upload_to=upload_to)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    