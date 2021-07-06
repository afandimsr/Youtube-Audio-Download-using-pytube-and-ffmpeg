from pytube import YouTube
from pytube.cli import on_progress
from pytube.helpers import safe_filename
import subprocess
import os


def run():
    try:
        videos_url = input("Please input video url : ")

        # make Youtube Object as yt
        yt = YouTube(videos_url, on_progress_callback=on_progress)

        # get title from yt object
        title = yt.title
        print("Downloading Audio From Title \"" + title + "\"")

        # get current folder
        path_download = os.getcwd() + "\Mp3 Download"

        # audio filter
        video = yt.streams.filter(only_audio=True).first()
        video.download(path_download)

        # get default file name
        default_filename = video.default_filename
        print(default_filename)

        # new_file_name_input = input("")
        new_safe_title = safe_filename(title)
        new_filename = new_safe_title + ".mp3"

       # convert audio using ffmpeg
        subprocess.run(['ffmpeg', "-i", os.path.join(path_download, default_filename),
                       os.path.join(path_download, new_filename)], shell=True)

        # remove mp4 file
        os.remove(path_download+"/" + default_filename)

        # Finish
        print("")
        print("============================================================")
        print("Download \"" + str(title) + "\" Completed ")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
