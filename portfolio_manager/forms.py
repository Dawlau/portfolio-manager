from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=120,
        required=True
    )

    first_name = forms.CharField(
        max_length=120,
        required=True
    )

    middle_name = forms.CharField(
        max_length=120,
        required=False
    )

    last_name = forms.CharField(
        max_length=120,
        required=True
    )

    birth_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            "class": "datepicker",
            "readonly": "readonly"
        })
    )

    address_line1 = forms.CharField(
        max_length=255,
        required=True,
        label="Address Line 1",
        widget=forms.TextInput(attrs={
            "placeholder": "123 Main St"
        })
    )

    address_line2 = forms.CharField(
        max_length=255,
        required=False,
        label="Address Line 2",
        widget=forms.TextInput(attrs={
            "placeholder": "Apt, suite, etc. (optional)"
        })
    )

    city = forms.CharField(
        max_length=120,
        required=True,
        label="City"
    )

    state_province_region = forms.CharField(
        max_length=120,
        required=True,
        label="State/Province/Region"
    )

    postal_code = forms.CharField(
        max_length=20,
        required=True,
        label="Postal Code/ZIP Code"
    )

    country = CountryField().formfield(
        placeholder="Select Country",
        widget=CountrySelectWidget(attrs={
            "class": "country-selector"
        })
    )

    tax_identification_number = forms.CharField(
        max_length=120,
        required=True
    )

    terms_acceptance = forms.BooleanField(
        label="I accept the terms and conditions.",
        required=True,
        initial=False,
        error_messages={
            "required": "You must accept the terms and conditions to register."
        },
        widget=forms.CheckboxInput(attrs={
            "class": "terms-checkbox"
        })
    )

    class Meta:
        model = User
        fields = (
            "username", "email", "first_name", "middle_name", "last_name",
            "birth_date", "address_line1", "address_line2", "city",
            "state_province_region", "postal_code", "country",
            "tax_identification_number", "password1", "password2",
            "terms_acceptance"
        )
