import re
from youtube_transcript_api import YouTubeTranscriptApi
from decouple import config
from google import genai
from google.genai import types

class YoutubeService:
    """ Handle Youtube related sevices"""

    @staticmethod
    def extract_video_id(url):
        """Extract video ID from YouTube URL"""
        patterns=[
            r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
            r'youtube\.com\/watch\?.*?v=([^&\n?#]+)'
        ]

        for pattern in patterns:
            match= re.search(pattern, url)
            if match:
                return match.group(1)
        return None
    
    @staticmethod
    def get_transcript(video_id):
        """Fetch transcript from YouTube"""
        try:
            api=YouTubeTranscriptApi()
            transcript_list = api.fetch(video_id).to_raw_data()
            transcript=' '.join([item['text'] for item in transcript_list])
            return transcript, None
        except Exception as e:
            
            return None, str(e)
        
class SummaryService:
    """Handle API summarization"""

    PROMPTS={
        'concise': 'Summarize this YouTube video transcript in 3-5 bullet points. Focus on the main ideas:',
        'detailed': 'Provide a detailed summary of this YouTube video transcript. Include main points, key arguments, and important details:',
        'tldr': 'Give me a TLDR (Too Long Didn\'t Read) of this YouTube video in 2-3 sentences:',
        'key_points': 'Extract the 5-10 most important key points from this YouTube video transcript as a numbered list:'
    }

    def __init__(self):
        api_key=config('GEMINI_API_KEY')
        self.client = genai.Client(api_key=api_key)
        self.model_id = "gemini-2.5-flash-lite"

    def summarize(self, transcript, summary_type='concise'):
        """Generate summary using Claude API"""
        prompt=self.PROMPTS.get(summary_type, self.PROMPTS['concise']) 

        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=f"{prompt}\n\n{transcript[:25000]}" 
            )
            return response.text, None
        except Exception as ex:
            print("TRANSCRIPT ERROR:", repr(ex)) 
            return None, str(ex)

        