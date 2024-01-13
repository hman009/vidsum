"""
__author__ : prakash ksd
description: The class represents a video summary application which
             receives a video file and based on the content shortern it

"""
import constants
from moviepy.editor import AudioFileClip,VideoFileClip
import librosa
import numpy as np
import matplotlib.pyplot as plt

class VideoSummary:

    CAPTURED_STAMPS = []
    CLIP_DURATION = 0
    SAMPLE_VID = "data/sample.mp4"
    AUDIO_FILE = "default.wav"


    def __init__(self,duration=15):
        # self.video_file = video_file
        print("starting application")
        self.max_duration = duration


    def audio_extractor(self):
        """
        This method will extract audio from a video file.
        """
        print("generating audio from video.....")
        audio_file = VideoFileClip(self.SAMPLE_VID)
        audio_file = audio_file.audio.write_audiofile("output.wav")

        return audio_file

    
    
    def calculate_audio_amplitude(self,input_audio,segment_duration=10):
        """
        This method will calulate the amplitude of each audio segement.
        :param - audio segment(part of a audio file)
        """
        y, sr = librosa.load(input_audio)
        print(y)
        print(sr)
        duration = librosa.get_duration(y=y, sr=sr)
        print(duration)

        segment_samples = int(segment_duration * sr)
        num_segments = int(duration / segment_duration)

        amplitudes = []

        for i in range(num_segments):
            start_sample = i * segment_samples
            end_sample = (i + 1) * segment_samples
            print(start_sample,end_sample)
            #handle for the last segment  
            segment_amplitude = np.max(np.abs(y[start_sample:end_sample]))
            amplitudes.append(segment_amplitude)

        return amplitudes




    def max_content_capture(self,segment=10,max_amplitude = 0):
        """
        This method based on the amplitude will capture the the audio parts with maximum content(audio wise)
        :param - segment duration which the audio clip will be divided in to
        :param - max amplitude limit 
        """
        pass



    def short_video_generator(self):
        """
        This method generates the short video from the timestamps which denotes the part of videos with maximum content.
        """    
        pass


    def generate_report(self):
        # plt.plot(amplitude)
        # a timetsamp range is required here 
        # plt.xlabel('Segment Index')
        # plt.ylabel('Amplitude')
        # plt.show()
        pass


    def summerize(self):
        """
        This method is the main method which all the other methods and generates the summarized file
        
        """
        # audio_file = self.audio_extractor()
        amplitude = self.calculate_audio_amplitude("output.wav")
        # print(amplitude)
        
        # self.CLIP_DURATION = audio_file.duration
        # print("CLIP DURATION : ",self.CLIP_DURATION)
        # data = []
        # print(audio_file.to_soundarray())
        return None







if __name__== "__main__":
    video_file = VideoSummary()
    video_file.summerize()    




