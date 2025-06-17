from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from catalog.models import Author
# from django.contrib.auth.admin import
# Register your models here.

# @admin.register(User)
# class UserAdmin(UserAdmin):
#     pass

@admin.register(Author)
class AuthorAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2","first_name", "last_name","email","phone","dob","dod"),
            },
        ),
    )
    list_display = ['first_name', 'last_name', 'email','phone','dob','dod']
    list_display_links = ['email','dod','dob']
    list_editable = ['first_name', 'last_name','phone']
