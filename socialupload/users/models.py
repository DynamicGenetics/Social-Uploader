import uuid
from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, EmailField, signals
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


# Set a random username for each user.
def random_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = uuid.uuid4().hex[:8]


class User(AbstractUser):
    # Add email as the replacement unique id field
    email = EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"

    # Add other required flags
    consent_granted = BooleanField(default=False)

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # https://stackoverflow.com/questions/11465293/create-a-field-whose-value-is-a-calculation-of-other-fields-values
    # https://www.reddit.com/r/django/comments/6xigr3/how_to_show_calculated_field_in_django_admin/

    # Register the properties
    # response_rate = property(_response_rate)
    # spotify_connected = property(_spotify_connected)

    # @property
    # def _response_rate(self):

    # @property
    # def _spotify_connected(self):


signals.pre_save.connect(random_username, sender=User)
