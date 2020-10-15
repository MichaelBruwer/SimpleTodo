from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# class item(models.Model):
#     name #name of the item that has to be completed
#     state #what process are you currently working 
#     date_posted = models.DateTimeField(default=timezone.now)
#     discrpition #more on what has to be done 
#     stage #what part of it you've completed what still needs to be done 


# class stage(models.Model):
#    Started = models.BooleanField(default=True, null=True)
#    Inprocess = models.BooleanField(default=False, null=True)
#    complete = models.BooleanField(default=False, null=True)


class List(models.Model):
    ListName = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    # stage = models.OneToOneField(stage, on_delete=models.CASCADE)

    def __str__(self):
        return self.ListName


    def get_absolute_url(self):
        return reverse('list-detail', kwargs={'pk': self.pk})