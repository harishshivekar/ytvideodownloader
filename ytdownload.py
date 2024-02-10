from pytube import YouTube


def download(link):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()

    try:
        yt.download()
    except:
        print("Some error is occurred")

    print("Downloaded successfully")

link = input("Enter the URL of video: ")
download(link)
