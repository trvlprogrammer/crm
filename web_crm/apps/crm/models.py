from django.db import models
from django.contrib.auth.models import User
from web_crm.models import abstract_fields 

class CRMTag(abstract_fields):    
    name = models.CharField(max_length=100)
    class Meta:
        db_table = "crm_tags"

    def __str__(self):
        return self.name

class CRMState(abstract_fields):    
    name = models.CharField(max_length=100)
    class Meta:
        db_table = "crm_state"

    def __str__(self):
        return self.name

class CRMLead(abstract_fields):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    date_deadline = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=250,null=True, blank=True)
    tags = models.ManyToManyField(CRMTag, blank=True)
    state = models.ForeignKey(CRMState, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        db_table = "crm_lead"
        indexes = [
            models.Index(fields=['user',]),
        ]

    def __str__(self):
        return self.name