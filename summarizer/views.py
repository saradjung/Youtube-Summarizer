from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import VideoSummary
from .forms import SummarizeForm
from .services import YoutubeService, SummaryService


# Create your views here.
def home(request):
    """Home page with form"""
    if request.method == 'POST':
        form=SummarizeForm(request.POST)
        if form.is_valid():
            summary_obj=form.save(commit=False)

            video_id=YoutubeService.extract_video_id(summary_obj.youtube_url)
            if not video_id:
                messages.error(request,'Invalid Youtube URL')
                return render(request, 'summarizer/home.html', {'form':form})
            
            summary_obj.video_id=video_id
            summary_obj.status='processing'
            summary_obj.save()

            youtube_service=YoutubeService()
            summary_service=SummaryService()

            transcript, error=youtube_service.get_transcript(video_id)
            if error:
                summary_obj.status="failed"
                summary_obj.error_message=f'Could not fetch the transcript:{error}'
                summary_obj.save()
                messages.error(request, 'Could not fetch video transcript. Make sure captions are enabled.')
                return render(request, 'summarizer/home.html', {'form': form})
            
            summary_obj.transcipt=transcript

            summary, error= summary_service.summarize(transcript,summary_obj.summary_type)
            if error:
                summary_obj.status = 'failed'
                summary_obj.error_message = f'Summarization failed: {error}'
                summary_obj.save()
                messages.error(request, 'Failed to generate summary. Please check your API key.')
                return render(request, 'summarizer/home.html', {'form': form})
            
            summary_obj.summary = summary
            summary_obj.status = 'completed'
            summary_obj.save()

            messages.success(request,"Summary generated successfully!")
            return redirect('summary_detail',pk=summary_obj.pk)
    else:
        form=SummarizeForm()

    recent_summaries=VideoSummary.objects.filter(status='completed')[:5]
    return render(request, 'summarizer/home.html',{
        'form':form,
        'recent_summaries':recent_summaries
    })

def summary_detail(request, pk):
    """Display individual summary"""
    summary = get_object_or_404(VideoSummary, pk=pk)
    return render(request, 'summarizer/summary_detail.html', {'summary': summary})

class SummaryListView(ListView):
    """List All Summaries"""

    model=VideoSummary
    template_name='summarizer/summary_list.html'
    context_object_name='summaries'
    paginate_by=10

    def get_queryset(self):
        return VideoSummary.objects.filter(status='completed')
    