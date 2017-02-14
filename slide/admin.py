# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import User
from slide.models import UserProfile
from slide.models import Folder
from slide.models import Song


class MemberAdmin(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1


class MyUserAdmin(UserAdmin):
    inlines = [MemberAdmin, ]


class FolderAdmin(admin.ModelAdmin):
    list_display = ('folderno', 'name')


class SongAdmin(admin.ModelAdmin):
    list_display = ('songid', 'title_1', 'writer', 'shrink_lyrics')

    def shrink_lyrics(self, obj):
        return obj.lyrics[:30] + '...'

    shrink_lyrics.short_description = 'Lyrics'


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Folder, FolderAdmin)
admin.site.register(Song, SongAdmin)
