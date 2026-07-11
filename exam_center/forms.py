from django import forms
from .models import ExamCenter


class ExamCenterForm(forms.ModelForm):

    class Meta:

        model = ExamCenter

        fields = "__all__"

        widgets = {

            "center_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter center name"
                }
            ),

            "center_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter center code"
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Enter address"
                }
            ),

            "city": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "state": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "pincode": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "contact_number": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "capacity": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }