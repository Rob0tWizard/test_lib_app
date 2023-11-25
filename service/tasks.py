from celery import shared_task
from django.core.mail import send_mail


from service.clients.models import CustomUser


@shared_task
def welcome_email(user_id):
    user = CustomUser().objects.get(pk=user_id)
    subject = 'Hello!'
    message = f'Thank you {user.username}, we will have a great journey together!'
    from_email = 'email-example@celery.com'
    to_email = [user.email]

    send_mail(subject, message, from_email, to_email)
