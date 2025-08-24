from django.contrib import admin

from .models import MemberUser, Activity, InfoOut


# Register your models here.

class AdminMemberUser(admin.ModelAdmin):
    list_display = (
        "username",
        "is_staff",
        "thumbnail",
        "in_community",
        "commission",
        "fonction",

    )
    list_editable = (
        "commission",
        "fonction",
        "in_community",
    )

class AdminActivity(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "begin",
        "end",
        "done",
    )

    list_editable = (
        "begin",
        "end",
        "done"
    )
class AdminInfoOut(admin.ModelAdmin):
    list_display = (
        'reason',
        'member',
        'done_at',
    )

admin.site.register(InfoOut,AdminInfoOut)
admin.site.register(MemberUser,AdminMemberUser)
admin.site.register(Activity,AdminActivity)
