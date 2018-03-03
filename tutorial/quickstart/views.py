# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from models import  Course, Curriculum, Group, Implement, GroupCourse, Room, Teacher, ImplementTeacher
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, CourseSerializer, CurriculumSerializer, \
    GroupSerializer, ImplementSerializer, GroupCourseSerializer, RoomSerializer, TeacherSerializer, \
    ImplementTeacherSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CurriculumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer




class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ImplementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Implement.objects.all()
    serializer_class = ImplementSerializer


class GroupCourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = GroupCourse.objects.all()
    serializer_class = GroupCourseSerializer


class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ImplementTeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = ImplementTeacher.objects.all()
    serializer_class = ImplementTeacherSerializer

