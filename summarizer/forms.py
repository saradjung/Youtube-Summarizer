from django import forms
from .models import VideoSummary

class SummarizeForm(forms.ModelForm):
    """Form for submitting YouTube URL"""

    class Meta:
        model=VideoSummary
        fields = ['youtube_url', 'summary_type']
        widgets={
            'youtube_url':forms.URLInput(attrs={
                "class":'form-control',
                'placeholder':'https://www.youtube.com/watch?v=...',
                'required':'True'
            }),
            'summary_type':forms.Select(attrs={
                'class':'form-select',
            }),
        }

        labels={
            'youtube_url': 'YouTube URL',
            'summary_type': 'Summary Type',
        }
    
    def clean_youtube_url(self):
        """Validate YouTube URL format"""
        url=self.cleaned_data.get('youtube_url')
        if 'youtube.com' not in url and 'youtu.be' not in url:
            raise forms.ValidationError("Please enter a vaild youtube URL")
        return url
