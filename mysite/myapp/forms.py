from django import forms
from myapp.models import MyUser
from django.contrib.auth.models import User
from myapp.models import UserProfileInfo


class NewUserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = MyUser
        fields=('first_name','last_name','email','password')

    def clean(self):
            cleaned_data = super(NewUserForm, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")
            if password != confirm_password:
                raise forms.ValidationError(
                    "password and confirm_password does not match"
                )



class DjangoUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('user_website','profile_pic')
