from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Crear equipos

        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Crear usuarios
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Crear actividades
        Activity.objects.create(user_email=tony.email, type='run', duration=30, date='2025-12-01')
        Activity.objects.create(user_email=steve.email, type='swim', duration=45, date='2025-12-02')
        Activity.objects.create(user_email=bruce.email, type='cycle', duration=60, date='2025-12-03')
        Activity.objects.create(user_email=clark.email, type='run', duration=50, date='2025-12-04')

        # Crear leaderboard
        Leaderboard.objects.create(team_name=marvel.name, points=200)
        Leaderboard.objects.create(team_name=dc.name, points=180)

        # Crear workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Plank', description='Hold plank for 1 min', difficulty='medium')
        Workout.objects.create(name='Burpees', description='Do 15 burpees', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
