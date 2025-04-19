# need to have ffmpeg installed in order for this to work

import os
from videoprops import get_video_properties

dir = '/mnt/video/'

def detect_video_codec(video_file):
    props = get_video_properties(video_file)

    if props['codec_name'] == "hevc":
        print(props['codec_name'], " - ", video_file)

if __name__ == "__main__":

    for root, dirs, files in os.walk(dir):
        for name in files:

            filename = os.path.join(root, name)

            if filename.endswith('.mp4') or filename.endswith('.mkv') or filename.endswith('.avi') or filename.endswith('.mpg'):
                detect_video_codec(filename)