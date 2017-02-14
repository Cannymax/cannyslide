# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from slide.models import Song
from rest_framework import viewsets, generics
from slide.serializers import UserSerializer, GroupSerializer, SongSerializer
from pagination import StandardResultsSetPagination


class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer,
    pagination_class = StandardResultsSetPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()[:20]
    serializer_class = SongSerializer
