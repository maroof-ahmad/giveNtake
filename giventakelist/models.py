from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class ListPost(models.Model):
    item = models.CharField(max_length=200, default="unnamed object")
    pub_date = models.DateTimeField('date',default=timezone.now)
    person = models.CharField(max_length=200, default= "anonymous person")
    ifreturned = models.BooleanField(default=False)
    return_date = models.DateTimeField('return date',blank=True,null=True)
    lendOrBorrow = models.BooleanField(default=False)
    def __str__(self):
        return (self.item)
    class Meta:
        ordering = ('ifreturned', 'pub_date')
