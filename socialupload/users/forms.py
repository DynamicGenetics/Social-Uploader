from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm


User = get_user_model()


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomSignupForm(SignupForm):
    # These are form items that aren't saved to a model instance.
    # However, we need people to indicate that they have understood before continuing.
    consent_granted = forms.BooleanField(
        initial=False,
        required=True,
        label="""I give my full consent for taking part in this research study.""",
    )

    # Specify the first couple of fields in this order. This appear at the top,
    # and then any unspecified fields are below.
    field_order = ["email", "password1", "password2"]

    def save(self, request):
        # Instructions https://django-allauth.readthedocs.io/en/latest/forms.html
        user = super(CustomSignupForm, self).save(request)

        # Note that email is saved through adapters.py to restrict non bristol addresses
        user.email = self.cleaned_data["email"]
        user.consent_granted = self.cleaned_data["consent_granted"]
        user.save()
        return user
