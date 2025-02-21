from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import leiloeiro

@receiver(post_save, sender=User)
def create_leiloeiro(sender, instance, created):
    if created:
        leiloeiro.objects.create(user=instance, nome=instance.username, email=instance.email)

@receiver(post_save, sender=User)
def save_leiloeiro(sender, instance):
    instance.leiloeiro.save()
