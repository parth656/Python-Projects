from pytube import YouTube

def download_video(url, output_path="."):
    try:

        youtube = YouTube(url)

        video_stream = youtube.streams.get_highest_resolution()

        video_stream.download(output_path)

        print(f"Video downloaded successfully to {output_path}")
    
    except Exception as e:
        print(f"Error: {e}")

video_url = "https://www.youtube.com/watch?v=example"
download_video(video_url, output_path="./downloads")
