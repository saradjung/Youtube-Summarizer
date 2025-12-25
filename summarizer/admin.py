from django.contrib import admin
from .models import VideoSummary

# Register your models here.
@admin.register(VideoSummary)
class VideoSummaryAdmin(admin.ModelAdmin):
    list_display=['video_id','summary_type','created_at','status']
    list_filter=['summary_type','created_at','status']
    search_fields=['video_id','youtube_url','summary']
    readonly_fields=['created_at','updated_at']