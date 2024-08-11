from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Special(models.Model):

    special_name = models.CharField(max_length=50)
    special_description = models.CharField(max_length=255)
    special_image = models.ImageField(upload_to ='special_images/(%Y-%m-%d)')

    class Meta:
        verbose_name = _("special")
        verbose_name_plural = _("specials")

    def __str__(self):
        return self.special_name

    def get_absolute_url(self):
        return reverse("special_detail", kwargs={"pk": self.pk})
    
    
class Chef(models.Model):

    chef_name = models.CharField(max_length=100)
    chef_description = models.CharField(max_length=255)
    chef_image = models.ImageField(upload_to ='shef_image/(%Y-%m-%d)')
    twitter_link = models.URLField(max_length=150)
    facebook_link = models.URLField(max_length=150)
    linkedin_link = models.URLField(max_length=150)

    class Meta:
        verbose_name = _("Chef")
        verbose_name_plural = _("Chefs")

    def __str__(self):
        return self.chef_name

    def get_absolute_url(self):
        return reverse("Chef_detail", kwargs={"pk": self.pk})


class Feedback(models.Model):

    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=400)
    

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")

    def __str__(self):
        return self.name (self.email)

    def get_absolute_url(self):
        return reverse("Feedback_detail", kwargs={"pk": self.pk})

