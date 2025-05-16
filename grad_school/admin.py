from django.contrib import admin

from .models import (
    Header,
    SectionsMenu,
    MenuItem,
    MainBanner,
    Features,
    BlockNames,
    Choosetab,
    Tabs,
    ComingSoon,
    Time,
    Registration,
    Section_courses,
    Section_video,
    Contact,
    FooterText
)


@admin.register(MainBanner)
class BannerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if MainBanner.objects.exists():
            return False

        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Time.objects.count() >= 4:
            return False

        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("title1","title2", "title3", 
                    "name", "email", "phon_number", 
                    "submitted_at")


@admin.register(Section_video)
class Section_videoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Section_video.objects.count() >= 1:
            return False

        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message", "submitted_at")


admin.site.register(Header)
admin.site.register(SectionsMenu)
admin.site.register(MenuItem)
admin.site.register(Features)
admin.site.register(BlockNames)
admin.site.register(Choosetab)
admin.site.register(Tabs)
admin.site.register(ComingSoon)
admin.site.register(Section_courses)
admin.site.register(FooterText)