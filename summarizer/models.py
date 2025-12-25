from django.db import models
from django.utils import timezone

# Create your models here.
class VideoSummary(models.Model):
    """Store YouTube video summaries"""
    
    SUMMARY_TYPES = [
        ('concise', 'Concise'),
        ('detailed', 'Detailed'),
        ('tldr', 'TLDR'),
        ('key_points', 'Key Points'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    #VIdeo info
    youtube_url=models.URLField(max_length=500)
    video_id=models.CharField(max_length=20, db_index=True)
    video_title=models.CharField(max_length=500, blank=True)

    #processing
    summary_type=models.CharField(max_length=20, choices=SUMMARY_TYPES, default='concise')
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    #content
    transcript=models.TextField(blank=True)
    summary=models.TextField(blank=True)

    #Metadata
    error_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']
        verbose_name_plural='Video Summaries'

    def __str__(self):
        return f"{self.video_id} - {self.get_summary_type_display()}"