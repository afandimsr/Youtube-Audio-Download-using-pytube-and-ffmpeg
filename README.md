# Download Audio format From YouTube using pytube and ffmpeg
## Description
Here I use Windows Operating system to make this package.
`pytube` Library is a command-line program to download videos from YouTube.com and a few more sites.
`ffmpeg` is A complete, cross-platform solution to record, convert and stream audio and video, For more details about ffmpeg, you can visit [Here](https://www.ffmpeg.org/about.html).
## Prerequisites
-  It requires the `Python interpreter, version 3.5` or higher python version.
-  ffmpeg, you can download [Windows](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z). or [Mac](https://evermeet.cx/ffmpeg/ffmpeg-102846-g6df4bcf1d0.zip). and [Linux(Ubuntu)](https://launchpad.net/ubuntu/+source/ffmpeg/) to another Linux Distribution You can See in [Here](https://www.ffmpeg.org/download.html).
## Steps
1. Clone this code.

        git clone https://github.com/afandimsr/Youtube-Audio-Download-using-pytube-and-ffmpeg.git

2. Make Virtual Environment you can see in  [Here](https://docs.python.org/3/tutorial/venv.html).
3. Active your Virtual Environment 
    - On Windows, run:

        `your-name-virtual-environtment\Scripts\activate.bat`

    - On Unix or MacOS, run:

        `source your-name-virtual-environtment/bin/activate`

4. Install pytube library 

        pip install pytube

5. Extract the downloaded ffmpeg file
6. Open Folder ffmpeg, Setup Environment Variable, if you never setup Environment variable, you can see here for [Windows](https://www.thewindowsclub.com/how-to-install-ffmpeg-on-windows-10). [Mac](https://medium.com/@himanshuagarwal1395/setting-up-environment-variables-in-macos-sierra-f5978369b255). [Linux](https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-environment-variables-in-linux/).
7. Open Terminal and Run `python downloader.py` or direct `downloader.py`

## License
This is code open-sourced software licensed under the [Apache-2.0](https://opensource.org/licenses/Apache-2.0).