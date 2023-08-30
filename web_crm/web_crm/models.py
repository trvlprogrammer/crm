from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class abstract_fields(models.Model):
    create_uid = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, related_name='%(class)s_created')
    write_uid = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True, related_name='%(class)s_modified')
    create_date = models.DateTimeField(null=True, blank=True, default=datetime.now())
    write_date = models.DateTimeField(null=True, blank=True, default=datetime.now())

    class Meta:
        abstract = True

