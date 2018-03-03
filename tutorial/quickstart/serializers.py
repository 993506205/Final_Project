from django.contrib.auth.models import User
from models import  Course, Curriculum, Group, Implement, GroupCourse, Room, Teacher, ImplementTeacher
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'code', 'name', 'type', 'language', 'credit', 'curriculumid', 'implementid')
		
class CurriculumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('url', 'period_total', 'p1', 'p2', 'p3', 'p4', 'p5', 'hour_factor', 'work_hour', 'amount_of_study_hours')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'code', 'degree_program')
		
class ImplementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Implement
        fields = ('url', 'id')
		
class GroupCourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupCourse
        fields = ('url', 'groupid', 'courseid')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'code', 'topic', 'courseid')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'code', 'name')
		
class ImplementTeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImplementTeacher
        fields = ('url', 'implementid', 'teacherid')
