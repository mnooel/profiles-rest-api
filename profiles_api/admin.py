from django.contrib import admin
from . import models as profiles_models

# Register your models here.
admin.site.register(profiles_models.UserProfile)
admin.site.register(profiles_models.ProfileFeedItem)
