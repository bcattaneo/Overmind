from django.db import models

class Replays(models.Model):
    title = models.CharField(max_length=200)
    base64_file = models.TextField()
    extra = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return '%s %s' % (self.title, self.base64_file)
        return (self.base64_file)