import os
from django.db import models

from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
import os

@deconstructible
class GenerateProfilePicturePath(object):
    def __init__(self):
        pass
    def __call__(self, instance, filename):
        ext=filename.split('.')[-1]
        #path=f'/media/zahid/Ads Power/Enterprise Infosec Consultants/{instance.user.id}'
        path = f'profile_pictures/{instance.user.id}'
        name=f'profile_image.{ext}'
        return os.path.join(path,name)
user_profile_image_path=GenerateProfilePicturePath()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.FileField(upload_to=user_profile_image_path, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

