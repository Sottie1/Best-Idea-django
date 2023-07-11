from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Work
from .mailchimp_utils import subscribe_user_to_mailchimp

# @receiver(post_save, sender=Work)
# def subscribe_user(sender, instance, created, **kwargs):
#     if created:
#         user_email = instance.request.user.email
#         subscribe_user_to_mailchimp(user_email)

# def subscribe_user(sender, work_item, **kwargs):
#     request = kwargs.get('request')
#     if request is not None:
#         user = request.user
#         work_item.subscribers.add(user)

def subscribe_user(sender, work_item, **kwargs):
    request = kwargs.get('request')
    if request is not None:
        user = request.user
        work_item.subscribers.add(user)

