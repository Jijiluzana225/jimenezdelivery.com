

# accounts/forms.py

from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    role = forms.ChoiceField(choices=[('customer', 'Customer'), ('store_owner', 'Store Owner')])

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data




from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



from django import forms
from .models import CustomerProfile

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = [
            'name', 'facebook_page', 'phone_number', 
            'barangay', 'address_line', 'location', 'profile_picture'
        ]


from django import forms
from .models import Store

class StoreOpenForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['open']
        widgets = {
            'open': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
        }


from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'type', 'description', 'price', 'picture', 'active']
        exclude = ['username']  # Exclude username since it's auto-assigned
        
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

