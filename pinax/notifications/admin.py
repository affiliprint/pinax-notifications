from django.contrib import admin

from .models import NoticeQueueBatch, NoticeSetting, NoticeType


class NoticeTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "label", "display", "description", "default"]


class NoticeSettingAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "notice_type", "medium", "scoping", "send"]
    list_filter = ["notice_type", "medium"]
    search_fields = ["user__email", "user__username"]


admin.site.register(NoticeQueueBatch)
admin.site.register(NoticeType, NoticeTypeAdmin)
admin.site.register(NoticeSetting, NoticeSettingAdmin)
