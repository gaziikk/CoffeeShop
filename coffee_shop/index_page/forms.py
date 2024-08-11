from django import forms
from .models import Special, Chef, Feedback

class SpecialForm(forms.ModelForm):
    
    class Meta:
        model = Special
        fields = ("special_name", "special_description", "special_image")
        labels = {
            'special_name': 'Название блюда',
            'special_description': 'Описание блюда',
            'special_image': 'Фотография блюда',
        }

class ChefForm(forms.ModelForm):
    
    class Meta:
        model = Chef
        fields = ("chef_name",
                  "chef_description",
                  "chef_image",
                  "twitter_link",
                  "facebook_link",
                  "linkedin_link")
        labels = {
            "chef_name": "Имя шеф-повара",
            "chef_description": "О себе",
            "chef_image": "Фотография",
            "twitter_link": "Ссылка на Twitter",
            "facebook_link": "Ссылка на Facebook",
            "linkedin_link": "Ссылка на Linkedin",
        }

class FeedBackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = ("first_name", "email", "message")
