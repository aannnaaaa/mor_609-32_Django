from django.dispatch import receiver
from django.db.models import signals
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from articles.models import Article


@receiver(signals.post_save, sender=Article)
def create_slug(sender, instance, **kwargs):
    slug_str = "%s %s" % (instance.title, get_random_string(length=4))
    if not instance.slug:
        print(f"Generating slug for {instance.title}")
        instance.slug = slugify(slug_str)

