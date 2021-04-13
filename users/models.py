from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from openings import models as opening_models
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

class Contact(models.Model):
    user_from = models.ForeignKey(User,related_name='rel_from_set',on_delete=models.CASCADE)
    user_to = models.ForeignKey(opening_models.Opening, related_name='rel_to_set',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False ))