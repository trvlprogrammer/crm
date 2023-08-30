from django.contrib import admin
from .models import CRMLead, CRMState, CRMTag
# Register your models here.
admin.site.register(CRMLead)
admin.site.register(CRMState)
admin.site.register(CRMTag)