# -*- coding: utf-8 -*-
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


class Course(models.Model):
    code = models.CharField(unique=True, max_length=10)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, blank=True, null=True)
    language = models.CharField(max_length=10)
    credit = models.IntegerField()
    curriculumid = models.ForeignKey('Curriculum', models.DO_NOTHING, db_column='curriculumid')  # Field name made lowercase.
    implementid = models.ForeignKey('Implement', models.DO_NOTHING, db_column='implementid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'


class Curriculum(models.Model):
    period_total = models.IntegerField(db_column='period total')  # Field renamed to remove unsuitable characters.
    p1 = models.IntegerField(db_column='P1', blank=True, null=True)  # Field name made lowercase.
    p2 = models.IntegerField(db_column='P2', blank=True, null=True)  # Field name made lowercase.
    p3 = models.IntegerField(db_column='P3', blank=True, null=True)  # Field name made lowercase.
    p4 = models.IntegerField(db_column='P4', blank=True, null=True)  # Field name made lowercase.
    p5 = models.IntegerField(db_column='P5', blank=True, null=True)  # Field name made lowercase.
    hour_factor = models.IntegerField(db_column='hour factor', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    work_hour = models.IntegerField(db_column='work hour', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    amount_of_study_hours = models.IntegerField(db_column='amount of study hours', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'curriculum'


class Group(models.Model):
    code = models.CharField(unique=True, max_length=10)
    degree_program = models.CharField(db_column='degree program', max_length=5)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'group'


class GroupCourse(models.Model):
    groupid = models.ForeignKey(Group, models.DO_NOTHING, db_column='groupid', primary_key=True)
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid')

    class Meta:
        managed = False
        db_table = 'group_course'
        unique_together = (('groupid', 'courseid'),)


class Implement(models.Model):
    id = models.IntegerField(db_column='id')

    class Meta:
        managed = False
        db_table = 'implement'


class ImplementTeacher(models.Model):
    implementid = models.ForeignKey(Implement, models.DO_NOTHING, db_column='implementid', primary_key=True)
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacherid')

    class Meta:
        managed = False
        db_table = 'implement_teacher'
        unique_together = (('implementid', 'teacherid'),)


class Room(models.Model):
    code = models.CharField(unique=True, max_length=10)
    topic = models.CharField(max_length=20)
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'


class Teacher(models.Model):
    code = models.CharField(unique=True, max_length=5)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'teacher'
