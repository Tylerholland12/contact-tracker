from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Function of Contacts
class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # Takes in contacts name
    name = models.CharField(max_length=100)
    # Takes in contacts email
    email = models.EmailField(max_length=100)
    # Takes in contacts phone number
    phone = models.IntegerField()
    # takes in any information about the contact
    info = models.CharField(max_length=100)
    # Take in number of connections you have similar to this contact
    connections = models.IntegerField()
    # Takes in contacts location
    contact_location = models.CharField(max_length=200)
    # Takes in Contacts gender
    gender = models.CharField(max_length=100, choices=(
        ('male','Male'),
        ('female','Female'),
        ("non-binary", 'Non-Binary'),
        ("choose-not-to-self-identify", 'Choose Not To Self Identify')
    ))
    # Takes in an image that this contact may have(placeholder will be used otherwise)
    image = models.ImageField(upload_to='images/',blank=True)
    # Date and time of connection
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
    