# -*- coding: utf-8 -*-
import sys
from django.db import models

reload(sys)
sys.setdefaultencoding('utf-8')


# 사용자 정보
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    nickname = models.CharField(u'닉네임', max_length=30)
    region = models.CharField(u'지역명', max_length=15, null=True, blank=True)
    gender = models.CharField(u'성별', max_length=3, null=True, blank=True)
    birthday = models.CharField(u'생년월일', max_length=12, null=True, blank=True)
    email = models.CharField(u'이메일', max_length=100, null=True, blank=True)
    is_login = models.BooleanField(u'로그인여부', default=False)

    def __unicode__(self):
        return u"%s" % (self.nickname)

    class Meta:
        verbose_name_plural = u"회원정보"
        verbose_name = u"회원정보"


# 폴더
class Folder(models.Model):
    folderno = models.SmallIntegerField(db_column='FolderNo', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    use = models.IntegerField(db_column='Use')  # Field name made lowercase.
    groupstyle = models.IntegerField(db_column='GroupStyle')  # Field name made lowercase.
    chorusheading = models.CharField(db_column='ChorusHeading', max_length=30, blank=True,
                                     null=True)  # Field name made lowercase.
    bridgeheading = models.CharField(db_column='BridgeHeading', max_length=30, blank=True,
                                     null=True)  # Field name made lowercase.
    endingheading = models.CharField(db_column='EndingHeading', max_length=30, blank=True,
                                     null=True)  # Field name made lowercase.
    vpos0 = models.IntegerField(db_column='VPos0', blank=True, null=True)  # Field name made lowercase.
    vpos1 = models.IntegerField(db_column='Vpos1', blank=True, null=True)  # Field name made lowercase.
    size0 = models.IntegerField(db_column='Size0', blank=True, null=True)  # Field name made lowercase.
    size1 = models.IntegerField(db_column='Size1', blank=True, null=True)  # Field name made lowercase.
    bold0 = models.IntegerField(db_column='Bold0', blank=True, null=True)  # Field name made lowercase.
    bold1 = models.IntegerField(db_column='Bold1', blank=True, null=True)  # Field name made lowercase.
    align0 = models.IntegerField(db_column='Align0', blank=True, null=True)  # Field name made lowercase.
    align1 = models.IntegerField(db_column='Align1', blank=True, null=True)  # Field name made lowercase.
    fontname0 = models.CharField(db_column='Fontname0', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    fontname1 = models.CharField(db_column='Fontname1', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    biu0 = models.CharField(db_column='BIU0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    biu1 = models.CharField(db_column='BIU1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cola = models.IntegerField(db_column='ColA', blank=True, null=True)  # Field name made lowercase.
    colb = models.IntegerField(db_column='ColB', blank=True, null=True)  # Field name made lowercase.
    bmargin = models.IntegerField(db_column='BMargin', blank=True, null=True)  # Field name made lowercase.
    biuheading = models.IntegerField(db_column='BIUHeading', blank=True, null=True)  # Field name made lowercase.
    headingsize = models.IntegerField(db_column='HeadingSize', blank=True, null=True)  # Field name made lowercase.
    headingoption = models.IntegerField(db_column='HeadingOption', blank=True, null=True)  # Field name made lowercase.
    linespacing = models.FloatField(db_column='LineSpacing', blank=True, null=True)  # Field name made lowercase.
    lmargin = models.IntegerField(db_column='LMargin', blank=True, null=True)  # Field name made lowercase.
    rmargin = models.IntegerField(db_column='RMargin', blank=True, null=True)  # Field name made lowercase.
    prechorusheading = models.CharField(db_column='PreChorusHeading', max_length=30, blank=True,
                                        null=True)  # Field name made lowercase.
    linespacing2 = models.FloatField(db_column='LineSpacing2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'folder'


# 곡 정보
class Song(models.Model):
    songid = models.IntegerField(db_column='SONGID', primary_key=True)  # Field name made lowercase.
    title_1 = models.CharField(db_column='TITLE_1', max_length=100)  # Field name made lowercase.
    title_2 = models.CharField(db_column='TITLE_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field1 = models.CharField(db_column='Field1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    writer = models.CharField(db_column='WRITER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    copyright = models.CharField(db_column='COPYRIGHT', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    lyrics = models.TextField(db_column='LYRICS')  # Field name made lowercase.
    sequence = models.TextField(db_column='SEQUENCE', blank=True, null=True)  # Field name made lowercase.
    key = models.CharField(db_column='KEY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=30, blank=True,
                                null=True)  # Field name made lowercase.
    folderno = models.SmallIntegerField(db_column='FOLDERNO')  # Field name made lowercase.
    oldfolder = models.SmallIntegerField(db_column='OLDFOLDER', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LASTMODIFIED')  # Field name made lowercase.
    msc = models.TextField(db_column='MSC', blank=True, null=True)  # Field name made lowercase.
    cjk_wordcount = models.CharField(db_column='CJK_WORDCOUNT', max_length=3, blank=True,
                                     null=True)  # Field name made lowercase.
    cjk_strokecount = models.CharField(db_column='CJK_STROKECOUNT', max_length=100, blank=True,
                                       null=True)  # Field name made lowercase.
    capo = models.IntegerField(db_column='CAPO', blank=True, null=True)  # Field name made lowercase.
    timing = models.CharField(db_column='TIMING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    song_number = models.IntegerField(db_column='SONG_NUMBER', blank=True, null=True)  # Field name made lowercase.
    licence_admin1 = models.CharField(db_column='LICENCE_ADMIN1', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.
    licence_admin2 = models.CharField(db_column='LICENCE_ADMIN2', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.
    book_reference = models.CharField(db_column='BOOK_REFERENCE', max_length=100, blank=True,
                                      null=True)  # Field name made lowercase.
    user_reference = models.TextField(db_column='USER_REFERENCE', blank=True, null=True)  # Field name made lowercase.
    settings = models.TextField(db_column='SETTINGS', blank=True, null=True)  # Field name made lowercase.
    formatdata = models.TextField(db_column='FORMATDATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'song'
