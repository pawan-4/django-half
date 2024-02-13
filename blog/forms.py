from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from .models import Post ,User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','category','tags')

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = '__all__'


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2','first_name','last_name']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User


#class MyCustomForm(forms.Form):
    
 ##  profile_picture = forms.ImageField(upload_to='profile_pics/', null=True, blank=True)
   # dob = forms.DateField(null=True, blank=True)
    #mobile_number = forms.CharField(max_length=15, null=True, blank=True)
    #about  = forms.TextField()
    #first_name =forms.TextField()
    #last_name =forms.TextFiel()