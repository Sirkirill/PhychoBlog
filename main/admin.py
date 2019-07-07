from django.contrib import admin
from django.contrib.auth.models import User, Group
from main.models import Achievement, Person, Article, Announcement, HelpItem


class PersonAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for person in queryset:
            person.delete()


admin.site.register(Person, PersonAdmin)
admin.site.register(Achievement)
admin.site.register(Article)
admin.site.register(Announcement)
admin.site.register(HelpItem)
# TODO admin.site.unregister(User)
# TODO admin.site.unregister(Group)
