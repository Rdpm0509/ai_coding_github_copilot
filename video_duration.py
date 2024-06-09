# generator that takes a irectory as an argument and 
# yields the duration of all the videos in the directory and all its subdirectories 

import os
from moviepy.editor import VideoFileClip

def absolute_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if f.endswith('.mp4'):
                yield os.path.abspath(os.path.join(dirpath, f))

def video_duration(directory):
    total_duration = 0 
    for file in absolute_file_paths(directory):
        clip = VideoFileClip(file)
        total_duration += clip.duration
    return total_duration/60 # return the total duration in minutes

path = r'D:\Videos'
d = video_duration(path)
print(f'Total duration of videos in {path} is {d} minutes')

# The function absolute_file_paths() is a generator that yields the absolute path of all the files with the extension .mp4 in the directory and all its subdirectories.

# print duration with onnly two decimal places
print(f'Total duration of videos in {path} is {d:.2f} minutes')
