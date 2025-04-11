from django.db import models
import uuid
from django.utils.deconstruct import deconstructible


# Create your models here.
import os
@deconstructible
class GenerateHouseImagePath(object):
    def __init__(self):
        pass
    def __call__(self, instances, filename):
        ext=filename.split('.')[-1]
        path=f'media/houses/{instances.id}/images'
        name=f'image.{ext}'
        return os.path.join(path,name)
    
house_image_path=GenerateHouseImagePath()

@deconstructible
class House(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=100)
    image=models.FileField(upload_to=house_image_path,blank=True, null=True)
    created_on=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    manager=models.OneToOneField('users.Profile',on_delete=models.SET_NULL,blank=True,null=True,related_name='managed_house')
    points=models.IntegerField(default=0)
    completed_tasks_count=models.IntegerField(default=0)
    pending_tasks_count=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} | {self.name}'

