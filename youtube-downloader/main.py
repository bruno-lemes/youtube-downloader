import os
import subprocess

from pytube import YouTube


def download_audio(link: str):
    yt = YouTube(link)
    audio = yt.streams.get_audio_only()
    path = audio.download( # type: ignore
        output_path='/home/bruno/Downloads/'
    ) 
    convert_video_to_audio(path)


def convert_video_to_audio(video_path: str):
    name = video_path.replace('.mp4', '.mp3')
    subprocess.run(['ffmpeg', '-i', video_path, name])
    os.remove(video_path)


def main():
    link = 'https://www.youtube.com/watch?v=6CXJ61UaDhE'
    # 'https://youtu.be/l2UDgpLz20M'
    download_audio(link)


if __name__ == '__main__':
    main()
