from django.core.files.storage import FileSystemStorage
from django.db import models

from core.constants import WORKER_STATUS_CHOICES, TASK_STATUS_CHOICES, RACE_CHOICES, PLAYER_TYPE_CHOICES


# Core app models storage, mostly specified for replays
fs = FileSystemStorage(location='media/')


class Worker(models.Model):
    """ Registered worker in the system """
    status = models.CharField(max_length=12, choices=WORKER_STATUS_CHOICES)
    name = models.CharField(max_length=100)
    last_known_ip = models.CharField(max_length=20)
    tasks = models.ManyToManyField('Task', through='TaskAssignment')

    def __str__(self):
        return "<Worker {} ({})>".format(self.id, self.name)


class TaskAssignment(models.Model):
    """ Task assignment to Worker """
    worker = models.ForeignKey('Worker', on_delete=None)
    task = models.ForeignKey('Task', on_delete=None)


class Task(models.Model):
    """ Task instance in the system """

    # Types of tasks
    REPLAY = 'replay'
    MATCH = 'match'

    # Waiting time before assigning other worker (in minutes)
    WAITING_TIME = 5

    status = models.CharField(max_length=12, choices=TASK_STATUS_CHOICES)
    max_retries = models.IntegerField()
    last_assigned = models.DateTimeField(blank=True, null=True, default=None)

    # Choose only one (restriction in the logic)
    replay = models.OneToOneField('Replay', on_delete=None)
    match = models.OneToOneField('Match', on_delete=None)

    @property
    def task_type(self):
        return Task.REPLAY if self.replay else Task.MATCH

    def __str__(self):
        return "<Task {}/{}>".format(self.id, self.task_type)


class Replay(models.Model):
    """ Match's replay, if human replay Match field won't be filled until replay processing is over """
    replay_file = models.FileField(storage=fs, upload_to="replays/")
    match = models.ForeignKey('Match', on_delete=None, blank=True, null=True)
    # TODO: Consider saving observations as JSONField here

    def __str__(self):
        if self.match:
            return "<Replay {}/M{}>".format(self.id, self.match_id)
        else:
            return "<Replay {}>".format(self.id)


class Match(models.Model):
    """ Match record in a particular date with certain players """
    players = models.ManyToManyField('Player', through='MatchPlayer')
    game_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "<Match {}>".format(self.id)


class MatchPlayer(models.Model):
    """ Player performing in a particular match, contains information about the player during match such as
        the player's id in that match and general stats.
    """
    match = models.ForeignKey('Match', on_delete=None)
    player = models.ForeignKey('Player', on_delete=None)

    id_in_match = models.IntegerField()
    win = models.BooleanField(default=False)
    # TODO: Add stats (more details)


class Player(models.Model):
    """ Player instance (race and type of player) """
    race = models.CharField(max_length=12, choices=RACE_CHOICES)
    player_type = models.CharField(max_length=20, choices=PLAYER_TYPE_CHOICES)

    def __str__(self):
        return "<Player {}/{}>".format(self.race, self.player_type)
