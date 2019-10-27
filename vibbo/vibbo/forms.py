from django.contrib.auth.models import User
from django import forms


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    bio = forms.CharField()

    street = forms.CharField()
    city = forms.CharField()
    location_code = forms.IntegerField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'bio',
            'street',
            'city',
            'location_code'
        )
