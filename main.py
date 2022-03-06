# Main imports
import os
from pytube import Playlist, YouTube

# Asking user for information
try:
    mode = int(input("\n\nWhat do you want to do?\n\n1. Download a youtube video\n2. Download a youtube playlist\n\nPlease provide the number: "))
    file_type = int(input("\n\nWhat file type do you want it to be saved?\n\n1. mp4\n2. mp3\n\nPlease provide the number: "))
    directory = input("\n\nPlease input the directory: \n\nexample: ./Musics\n\nDirectory: ")
except:
    temp = input("\n\nPlease provide a integer as example. (press enter to exit)")

# Checking if all information are provided
try:
    if mode == "":
        temp = input("\n\nPlease provide a integer as example. (press enter to exit)")
    if file_type == "":
        temp = input("\n\nPlease provide a integer as example. (press enter to exit)")
except:
    temp = input("\n\nPlease provide a integer as example. (press enter to exit)")

# Specifying the file type
if file_type == 1:
    file_type = ".mp4"
else:
    file_type = ".mp3"

# Downloader
def download(video, video_number):
    failed = ""
    print(f"#{video_number} [+] Downloading {video.title}")
    try:
        video_output = video.streams.filter(only_audio=True).first()
        downloaded_file = video_output.download(directory)
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + file_type
        os.rename(downloaded_file, new_file)
    except FileExistsError:
        print(f"#{video_number} [-] Ignoring {video.title} due to file already exist")
        try:
            os.remove(f"{directory}/{video.title}.mp4")
        except FileNotFoundError:
            print(f"#{video_number} [-] Problem in deleting file. Please delete {video.title}.mp4 manually")
        except OSError:
            print(f"#{video_number} [-] Problem in deleting file. Please delete {video.title}.mp4 manually")
    except Exception as e:
        print(f"#{video_number} [-] Something went wrong with {video.title} - {e}")
        failed += f"#{video_number} - {video.title}\n"
        try:
            os.remove(f"{directory}/{video.title}.mp4")
        except FileNotFoundError:
            print(f"#{video_number} [-] Problem in deleting file. Please delete {video.title}.mp4 manually")
        except OSError:
            print(f"#{video_number} [-] Problem in deleting file. Please delete {video.title}.mp4 manually")
    return failed

# Specific video downloader
if mode == 1:
    video = YouTube(input("\n\nVideo link: "))
    failed = ""
    failed += download(video=video, video_number=1)
    print(f"\n\n[+] DONE DOWNLOADING\n\n[-] Failed downloads\n\n{failed}")

# Playlist downloader
elif mode == 2:
    playlist = Playlist(input("\n\nPlaylist link: "))
    video_number = 0
    failed = ""
    for video in playlist.videos:
        video_number += 1
        failed += download(video=video, video_number=video_number)
    print(f"\n\n[+] DONE DOWNLOADING\n\n[-] Failed downloads\n\n{failed}")
