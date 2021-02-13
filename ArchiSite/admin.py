from django.contrib import admin
from django.contrib.auth.models import Group
from django import forms

from .models import *

admin.site.register(Portfolio)
admin.site.register(HousePlans)
admin.site.register(NewsletterList)
admin.site.register(Applications)
admin.site.register(Blog)