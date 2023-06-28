from django.core.mail import mail_admins
from celery import shared_task


@shared_task()
def send_to_admin(subject, message):
    print('mail_admins')
    mail_admins(
        subject,
        message,
    )


@shared_task()
def send_email_report():
    print('Send report')
