from django.conf import settings
from mailchimp3 import MailChimp

def subscribe_user_to_mailchimp(email):
    client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY)
    list_id = settings.MAILCHIMP_LIST_ID

    client.lists.members.create(list_id, {
        'email_address': email,
        'status': 'subscribed',
    })
