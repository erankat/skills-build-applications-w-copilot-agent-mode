from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # Use 'id' instead of '_id'

class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField()
    members = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration']  # Use 'id' instead of '_id'

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Use UserSerializer to include user details

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'score']

class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField()

    class Meta:
        model = Workout
        fields = '__all__'
