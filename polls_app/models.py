from django.db import models
from django.conf import settings
from django.urls import reverse


class Polls(models.Model):
    class Meta:
        verbose_name_plural = "Polls"

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.CharField(max_length=200, null=False, blank=False)
    choice1 = models.CharField(max_length=200, null=False, blank=False)
    choice2 = models.CharField(max_length=200, null=False, blank=False)
    choice3 = models.CharField(max_length=200, null=False, blank=False)
    choice1_count = models.PositiveIntegerField(default=0)
    choice2_count = models.PositiveIntegerField(default=0)
    choice3_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question[:50]  # display first 50 characters of field

    def get_absolute_url(self):
        return reverse("poll_detail", kwargs={"pk": self.pk})

    def total(self):
        return self.choice1_count + self.choice2_count + self.choice3_count
