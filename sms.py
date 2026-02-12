import os
import sys
import time
import shutil
import yt_dlp


GREEN = "\033[1;32m"
RESET = "\033[0m"

def animated_logo(delay=0.001):
    logo = r"""
 MM    d'  @6MMMMb  `MMMMMMMb.`MM`MMMMMMMb.
 MM   d'  8P    Y8  MM    `Mb MM MM    `Mb
 MM  d'  6M      Mb MM     MM MM MM     MM
 MM d'   MM      MM MM    .M9 MM MM     MM
 MMd'    MM      MM MMMMMMM(  MM MM    .M9
 MMYM.   MM      MM MM    `Mb MM MMMMMMM9'
 MM YM.  MM      MM MM     MM MM MM  \M\
 MM  YM. YM      M9 MM     MM MM MM   \M\
 MM   YM. 8b    d8  MM    .M9 MM MM    \M\
_MM_   YM._YMMMM9  _MMMMMMM9'_MM_MM_    \M\_

      CREDIT = SK KOBIR VAI
      Bangladesh Cyber King
      All Video Download Tools
    """
    for char in logo:
        sys.stdout.write(f"{GREEN}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def download_video(url):

    download_path = os.path.expanduser("~/storage/shared/Download/py_videos")
    os.makedirs(download_path, exist_ok=True)

    ffmpeg_path = shutil.which("ffmpeg")

    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
        
        'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    if ffmpeg_path:
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'postprocessors': [{'key': 'FFmpegMetadata'}, {'key': 'EmbedThumbnail'}],
        })
    else:
        
        ydl_opts['format'] = 'best[ext=mp4]/best'

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"{GREEN}Starting download...{RESET}")
            ydl.download([url])
            print(f"\n{GREEN}Download completed successfully!{RESET}")
    except Exception as e:
        print(f"\n\033[1;31mError: {str(e)}{RESET}")

if __name__ == "__main__":
    animated_logo()
    video_url = input(f"{GREEN}Enter video URL: {RESET}").strip()
    if video_url:
        download_video(video_url)
    else:
        print("No URL provided!")
