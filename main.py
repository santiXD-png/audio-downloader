import yt_dlp
url = input("Pega la URL: ")
options = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3'}]}
with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])
