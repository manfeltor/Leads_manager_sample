from django import forms
from .models import FormSubmission
from usersapp.models import CustomUser  # Import your custom user model

class FormSubmissionEditForm(forms.ModelForm):
    assigned_user = forms.ModelChoiceField(queryset=CustomUser.objects.filter(role='employee'), required=False)

    class Meta:
        model = FormSubmission
        fields = [
            'razon_social', 'nombre_y_apellido', 'telefono', 
            'estado', 'assigned_user', 'management_message'
        ]