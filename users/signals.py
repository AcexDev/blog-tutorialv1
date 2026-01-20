from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save, sender=User)
def create_post(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_post(sender, instance, created, **kwargs):
    instance.profile.save()