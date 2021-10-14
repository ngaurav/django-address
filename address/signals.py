from django.db.models.signals import post_save
from django.dispatch import receiver

from address.models import Address


@receiver(post_save, sender=Address)
def populate_formatted(sender, instance, created, **kwargs):
    """If "formatted" is empty try to construct it from other values."""
    if created and not instance.formatted:
        instance.formatted = str(instance)
