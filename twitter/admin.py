from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group, User
from .models import Profile, Twitter

# Register your models here.
class ProfileInline(admin.StackedInline):
  model = Profile
class UserAdmin(ModelAdmin):
  model = User
  fields= ["username"]
  inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Twitter)
# admin.site.register(Profile)
admin.site.unregister(Group)