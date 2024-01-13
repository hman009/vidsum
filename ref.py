from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import numpy as np

# Load the video
clip = VideoFileClip("data/sample.mp4")

# Extract audio
audio = clip.audio.to_soundarray()

# Split audio into segments (e.g., 10 seconds each)
# segment_duration = 10  # in seconds
# segment_size = int(segment_duration * clip.fps)
# num_segments = audio.shape[0] // segment_size
#
# # Initialize list to store segments with speech
# segments_with_speech = []
#
# # Analyze each segment
# for i in range(num_segments):
#     start = i * segment_size
#     end = (i + 1) * segment_size
#
#     # Check if there is significant audio (you may need to adjust the threshold)
#     if np.max(np.abs(audio[start:end])) > 0.05:
#         segments_with_speech.append((start / clip.fps, end / clip.fps))
#
# # Concatenate segments with speech
# final_audio = AudioSegment.silent(duration=0)
# for start, end in segments_with_speech:
#     final_audio += clip.audio.subclip(start, end)
#
# # Set the audio of the original clip to the final audio
# clip = clip.set_audio(final_audio)
#
# # Generate the final video
# clip.write_videofile("output_video.mp4")