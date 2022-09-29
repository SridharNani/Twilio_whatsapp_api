from django.db import models
from twilio.rest import Client
#
# # Create your models here.
#
#
class Score(models.Model):
    #integer field
    test_result = models.PositiveIntegerField()

    #string representation
    def __str__(self):
        return str(self.test_result)

    def save(self, *args, **kwargs):
        # if test_result is less than 80 execute this
        if self.test_result < 80:
            # twilio code
            account_sid = 'AC6489af9797220c83c7a4a8abdc5b8226'
            auth_token = 'b936b0f1eef07fb5c238cca412275d02'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'Hi, your test result is {self.test_result}. Great job',
                from_='+18103799623',
                to='+918143510050'
            )

            print(message.sid)
        return super().save(*args, **kwargs)

