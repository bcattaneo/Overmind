from django.db import models

# Game replays
class Replays(models.Model):
    title = models.CharField(max_length=200)
    base64_file = models.TextField()
    extra = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("%s" % (self.title))

    class Meta:
        indexes = [
            models.Index(fields=['title', 'date'])
        ]

# Replays assignments
class Assign(models.Model):
    replay = models.ForeignKey(Replays, on_delete=None)
    overlord = models.CharField(max_length=200)         # overlord unique ID
    update = models.DateTimeField(auto_now_add=True)    # update date
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("%s - %s" % (self.replay, self.overlord))

    class Meta:
        indexes = [
            models.Index(fields=['replay', 'overlord', 'date', 'update'])
        ]