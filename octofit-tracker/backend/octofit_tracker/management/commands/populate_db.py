from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data using raw SQL to truncate tables
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM octofit_tracker_activity;')
            cursor.execute('DELETE FROM octofit_tracker_leaderboard;')
            cursor.execute('DELETE FROM octofit_tracker_workout;')
            cursor.execute('DELETE FROM octofit_tracker_team_members;')
            cursor.execute('DELETE FROM octofit_tracker_team;')
            cursor.execute('DELETE FROM octofit_tracker_user;')

        # Create users
        users = [
            User(username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(username='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
            User(username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)
        saved_users = list(User.objects.all())

        # Create a team and add members
        team = Team(name='Blue Team')
        team.save()
        team.members.set(User.objects.all())

        # Create activities
        activities = [
            Activity(user=saved_users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(user=saved_users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity(user=saved_users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(user=saved_users[3], activity_type='Strength', duration=timedelta(minutes=30)),
            Activity(user=saved_users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=saved_users[0], score=100),
            Leaderboard(user=saved_users[1], score=90),
            Leaderboard(user=saved_users[2], score=95),
            Leaderboard(user=saved_users[3], score=85),
            Leaderboard(user=saved_users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
