from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=50, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    expiry_date = models.DateField(null=True, blank=True)
    apply_link = models.URLField(max_length=200, blank=True)
    category = models.CharField(
        max_length=50,
        choices=(
            ('python', 'Python'),
            ('django', 'Django'),
            ('react', 'React'),
            ('remote', 'Remote'),
        )
    )
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return f"{self.title} at {self.company}"

    def is_expired(self):
        if self.expiry_date:
            return timezone.now().date() > self.expiry_date
        return False
