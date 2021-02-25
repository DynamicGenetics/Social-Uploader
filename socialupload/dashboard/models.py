from django.contrib.auth import get_user_model
from django.db import models


class FullUserHistory(models.Model):
    """This table will hold the data submitted by the user at the end of
    the experiment that is sent to them by Spotify. It will be sent in
    JSON format with the four fields placed here.
    """

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="uploaded_history"
    )
    end_time = models.DateTimeField()
    artist = models.CharField(max_length=600)
    track_name = models.CharField(max_length=600)
    ms_played = models.IntegerField()
    time_added = models.DateTimeField(auto_now_add=True)
