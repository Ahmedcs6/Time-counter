import pytube
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def get_video_data(url):
    try:
        yt = pytube.YouTube(url)
        duration = yt.length
        return url, duration
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return None, None

def main():
    print("=" * 45)
    print("=" * 12 + "YouTube Playlist Duration Calculator" + "=" * 12)
    print("=" * 45)

    while True:
        try:
            url = input("Enter a YouTube playlist URL: ")
            # Validate URL format (basic check)
            if not url.startswith("https://www.youtube.com/playlist?"):
                print("Invalid URL format. Please enter a valid YouTube playlist URL.")
                continue

            playlist = pytube.Playlist(url)
            video_urls = [video.watch_url for video in playlist.videos]

            with ThreadPoolExecutor(max_workers=5) as executor:
                futures = [executor.submit(get_video_data, video_url) for video_url in video_urls]
                total_duration = 0
                processed = 0

                # ... rest of the code for progress bar, processing, etc. (unchanged)

            break  # Exit loop on successful execution

        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again with a valid YouTube playlist URL.")

if __name__ == "__main__":
    main()
